"""
Lexer → Parser → Compiler → Evaluator Pipeline

Implements a complete expression processing pipeline:
  1. Lexer   — tokenizes raw source into a stream of typed tokens
  2. Parser  — builds an Abstract Syntax Tree via recursive descent
  3. Compiler — lowers the AST into stack-based bytecode instructions
  4. Evaluator — executes bytecode on a register-free stack machine

Supports: integer/float literals, identifiers, assignment (=),
          arithmetic (+, -, *, /, //, %, **), parenthesised grouping.
"""

from __future__ import annotations

import io
import struct
import time
import binascii
import marshal
import tokenize as _stdlib_tokenize
import ast as _stdlib_ast
import dis as _stdlib_dis
from enum import Enum, auto
from typing import Any, Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from pprint import pp


# ─────────────────────────────────────────────────────────────────────
# Token Representation
# ─────────────────────────────────────────────────────────────────────

class TokenType(Enum):
    """Enumeration of all token categories recognised by the lexer."""
    NUMBER    = auto()
    NAME      = auto()
    OP        = auto()
    LPAREN    = auto()
    RPAREN    = auto()
    ASSIGN    = auto()
    ENDMARKER = auto()


@dataclass(frozen=True, slots=True)
class Token:
    """Immutable, position-aware token produced by the lexer."""
    type: TokenType
    value: str
    position: int        # character offset in the source string

    def __repr__(self) -> str:
        return f"Token({self.type.name}, {self.value!r}, pos={self.position})"


# ─────────────────────────────────────────────────────────────────────
# AST Node Hierarchy
# ─────────────────────────────────────────────────────────────────────

class ASTNode:
    """Base class for every node in the abstract syntax tree."""


@dataclass(slots=True)
class NumberLiteral(ASTNode):
    value: int | float

    def __repr__(self) -> str:
        return f"Constant(value={self.value})"


@dataclass(slots=True)
class Identifier(ASTNode):
    name: str
    ctx: str = "Load"

    def __repr__(self) -> str:
        return f"Name(id={self.name!r}, ctx={self.ctx}())"


@dataclass(slots=True)
class BinaryOp(ASTNode):
    left: ASTNode
    op: str
    right: ASTNode

    _OP_NAMES = {"+": "Add", "-": "Sub", "*": "Mult", "/": "Div",
                 "//": "FloorDiv", "%": "Mod", "**": "Pow"}

    def __repr__(self) -> str:
        op_name = self._OP_NAMES.get(self.op, self.op)
        return f"BinOp(left={self.left}, op={op_name}(), right={self.right})"


@dataclass(slots=True)
class UnaryOp(ASTNode):
    op: str
    operand: ASTNode

    def __repr__(self) -> str:
        return f"UnaryOp(op={'USub' if self.op == '-' else 'UAdd'}(), operand={self.operand})"


@dataclass(slots=True)
class Assignment(ASTNode):
    target: Identifier
    value: ASTNode

    def __repr__(self) -> str:
        store_target = Identifier(self.target.name, ctx="Store")
        return f"Assign(targets=[{store_target}], value={self.value})"


# ─────────────────────────────────────────────────────────────────────
# Bytecode Instruction Set
# ─────────────────────────────────────────────────────────────────────

class OpCode(Enum):
    """Stack-machine opcodes emitted by the compiler."""
    LOAD_CONST   = auto()
    LOAD_NAME    = auto()
    STORE_NAME   = auto()
    BINARY_ADD   = auto()
    BINARY_SUB   = auto()
    BINARY_MUL   = auto()
    BINARY_DIV   = auto()
    BINARY_FLOOR = auto()
    BINARY_MOD   = auto()
    BINARY_POW   = auto()
    UNARY_NEG    = auto()
    UNARY_POS    = auto()
    RETURN_VALUE = auto()


@dataclass(frozen=True, slots=True)
class Instruction:
    """Single bytecode instruction with an optional operand."""
    opcode: OpCode
    arg: Any = None

    def __repr__(self) -> str:
        if self.arg is not None:
            return f"{self.opcode.name:<18} {self.arg!r}"
        return self.opcode.name


# ─────────────────────────────────────────────────────────────────────
# Operator Precedence & Dispatch Tables
# ─────────────────────────────────────────────────────────────────────

_OPERATOR_TO_OPCODE: Dict[str, OpCode] = {
    "+":  OpCode.BINARY_ADD,
    "-":  OpCode.BINARY_SUB,
    "*":  OpCode.BINARY_MUL,
    "/":  OpCode.BINARY_DIV,
    "//": OpCode.BINARY_FLOOR,
    "%":  OpCode.BINARY_MOD,
    "**": OpCode.BINARY_POW,
}

_OPCODE_TO_CALLABLE = {
    OpCode.BINARY_ADD:   lambda a, b: a + b,
    OpCode.BINARY_SUB:   lambda a, b: a - b,
    OpCode.BINARY_MUL:   lambda a, b: a * b,
    OpCode.BINARY_DIV:   lambda a, b: a / b,
    OpCode.BINARY_FLOOR: lambda a, b: a // b,
    OpCode.BINARY_MOD:   lambda a, b: a % b,
    OpCode.BINARY_POW:   lambda a, b: a ** b,
}


# ─────────────────────────────────────────────────────────────────────
# Custom Exception Hierarchy
# ─────────────────────────────────────────────────────────────────────

class PipelineError(Exception):
    """Base exception for the lexer/parser/compiler/evaluator pipeline."""


class LexerError(PipelineError):
    def __init__(self, message: str, position: int):
        super().__init__(f"LexerError at position {position}: {message}")
        self.position = position


class ParserError(PipelineError):
    def __init__(self, message: str, token: Token | None = None):
        loc = f" at {token}" if token else ""
        super().__init__(f"ParserError{loc}: {message}")
        self.token = token


class CompilerError(PipelineError):
    pass


class EvaluatorError(PipelineError):
    pass


# ═════════════════════════════════════════════════════════════════════
# Main Pipeline Class
# ═════════════════════════════════════════════════════════════════════

class LexerExampleWithExpressionKnown:
    def __init__(self, expression):
        self.expression = expression
        self.tokens = []
        self.current_position = 0
        self._ast: ASTNode | None = None
        self._bytecode: List[Instruction] = []
        self._environment: Dict[str, Any] = {}
#expr='x=2+2'
    def tokenize(self):
        # Tokenization logic goes here
        # import tokenize
        # strIO = io.StringIO(self.expression).readline
        # tokens = tokenize.generate_tokens(strIO)
        # pp(list(tokens))
        # [
            # TokenInfo(type=NAME, string='x'),
            # TokenInfo(type=OP, string='='),
            # TokenInfo(type=NUMBER, string='2'),
            # TokenInfo(type=OP, string='+'),
            # TokenInfo(type=NUMBER, string='2'),
            # TokenInfo(type=ENDMARKER, string=''),
        # ]
        self.tokens.clear()
        self.current_position = 0
        src = self.expression
        length = len(src)
        pos = 0

        while pos < length:
            ch = src[pos]

            # ── skip whitespace ──
            if ch.isspace():
                pos += 1
                continue

            # ── numeric literal (int or float) ──
            if ch.isdigit() or (ch == '.' and pos + 1 < length and src[pos + 1].isdigit()):
                start = pos
                has_dot = False
                while pos < length and (src[pos].isdigit() or src[pos] == '.'):
                    if src[pos] == '.':
                        if has_dot:
                            raise LexerError("Malformed numeric literal (multiple decimal points)", pos)
                        has_dot = True
                    pos += 1
                # handle exponent notation  e.g. 3e10, 2.5E-3
                if pos < length and src[pos] in ('e', 'E'):
                    pos += 1
                    if pos < length and src[pos] in ('+', '-'):
                        pos += 1
                    if pos >= length or not src[pos].isdigit():
                        raise LexerError("Invalid exponent in numeric literal", pos)
                    while pos < length and src[pos].isdigit():
                        pos += 1
                self.tokens.append(Token(TokenType.NUMBER, src[start:pos], start))
                continue

            # ── identifier / keyword ──
            if ch.isalpha() or ch == '_':
                start = pos
                while pos < length and (src[pos].isalnum() or src[pos] == '_'):
                    pos += 1
                self.tokens.append(Token(TokenType.NAME, src[start:pos], start))
                continue

            # ── multi-character operators ──
            two_char = src[pos:pos + 2]
            if two_char in ('//', '**'):
                self.tokens.append(Token(TokenType.OP, two_char, pos))
                pos += 2
                continue

            # ── single-character operators and delimiters ──
            if ch == '(':
                self.tokens.append(Token(TokenType.LPAREN, ch, pos))
                pos += 1
                continue
            if ch == ')':
                self.tokens.append(Token(TokenType.RPAREN, ch, pos))
                pos += 1
                continue
            if ch == '=':
                self.tokens.append(Token(TokenType.ASSIGN, ch, pos))
                pos += 1
                continue
            if ch in ('+', '-', '*', '/', '%'):
                self.tokens.append(Token(TokenType.OP, ch, pos))
                pos += 1
                continue

            raise LexerError(f"Unexpected character {ch!r}", pos)

        self.tokens.append(Token(TokenType.ENDMARKER, '', pos))
        return self.tokens

    def get_next_token(self):
        # Logic to get the next token from the source code
        # if self.current_position < len(self.tokens):
            # token = self.tokens[self.current_position]
            # self.current_position += 1
            # return token
        # return None
        if self.current_position < len(self.tokens):
            token = self.tokens[self.current_position]
            self.current_position += 1
            return token
        return None

    def peek_next_token(self):
        # Logic to peek at the next token without consuming it
        # if self.current_position < len(self.tokens):
            # return self.tokens[self.current_position]
        # return None
        if self.current_position < len(self.tokens):
            return self.tokens[self.current_position]
        return None

    # ── Recursive-Descent Parser ────────────────────────────────────
    #
    # Grammar (precedence low → high):
    #
    #   statement   → NAME '=' expression | expression
    #   expression  → term (('+' | '-') term)*
    #   term        → exponent (('*' | '/' | '//' | '%') exponent)*
    #   exponent    → unary ('**' exponent)?          (right-associative)
    #   unary       → ('+' | '-') unary | atom
    #   atom        → NUMBER | NAME | '(' expression ')'
    #

    def _parse_atom(self) -> ASTNode:
        """Parse an atomic expression: literal, identifier, or parenthesised group."""
        token = self.peek_next_token()
        if token is None or token.type == TokenType.ENDMARKER:
            raise ParserError("Unexpected end of expression", token)

        if token.type == TokenType.NUMBER:
            self.get_next_token()
            value = float(token.value) if ('.' in token.value or 'e' in token.value.lower()) else int(token.value)
            return NumberLiteral(value)

        if token.type == TokenType.NAME:
            self.get_next_token()
            return Identifier(token.value)

        if token.type == TokenType.LPAREN:
            self.get_next_token()  # consume '('
            node = self._parse_expression()
            closing = self.get_next_token()
            if closing is None or closing.type != TokenType.RPAREN:
                raise ParserError("Expected closing ')'", closing)
            return node

        raise ParserError(f"Unexpected token {token}", token)

    def _parse_unary(self) -> ASTNode:
        """Parse unary +/- prefix operators."""
        token = self.peek_next_token()
        if token and token.type == TokenType.OP and token.value in ('+', '-'):
            self.get_next_token()
            operand = self._parse_unary()
            # constant-fold trivial unary on literals
            if isinstance(operand, NumberLiteral) and token.value == '-':
                return NumberLiteral(-operand.value)
            if isinstance(operand, NumberLiteral) and token.value == '+':
                return operand
            return UnaryOp(token.value, operand)
        return self._parse_atom()

    def _parse_exponent(self) -> ASTNode:
        """Parse right-associative exponentiation (**)."""
        base = self._parse_unary()
        token = self.peek_next_token()
        if token and token.type == TokenType.OP and token.value == '**':
            self.get_next_token()
            exponent = self._parse_exponent()  # right-associative recursion
            return BinaryOp(base, '**', exponent)
        return base

    def _parse_term(self) -> ASTNode:
        """Parse multiplicative operators: *, /, //, %."""
        node = self._parse_exponent()
        while True:
            token = self.peek_next_token()
            if token and token.type == TokenType.OP and token.value in ('*', '/', '//', '%'):
                self.get_next_token()
                right = self._parse_exponent()
                node = BinaryOp(node, token.value, right)
            else:
                break
        return node

    def _parse_expression(self) -> ASTNode:
        """Parse additive operators: +, -."""
        node = self._parse_term()
        while True:
            token = self.peek_next_token()
            if token and token.type == TokenType.OP and token.value in ('+', '-'):
                self.get_next_token()
                right = self._parse_term()
                node = BinaryOp(node, token.value, right)
            else:
                break
        return node

    def _parse_statement(self) -> ASTNode:
        """Parse a top-level statement (assignment or bare expression)."""
        saved_pos = self.current_position
        token = self.peek_next_token()

        # Try  NAME '=' expression
        if token and token.type == TokenType.NAME:
            name_token = self.get_next_token()
            eq_token = self.peek_next_token()
            if eq_token and eq_token.type == TokenType.ASSIGN:
                self.get_next_token()  # consume '='
                value_node = self._parse_expression()
                return Assignment(Identifier(name_token.value, ctx="Store"), value_node)
            # Not an assignment — backtrack
            self.current_position = saved_pos

        return self._parse_expression()

    def parse_expression(self):
        # Logic to parse the expression based on the tokens
        # This is where you would implement your parsing logic
        #import ast
        #tree = ast.parse(self.expression, mode='eval')
        #ast.dump(tree)
#       Module(
#         body=[
#                Assign(targets=[Name(id='x', ctx=Store())], value=BinOp(left=Constant(value=2), op=Add(), right=Constant(value=2)))
#               )
#               )
#               ]
#               )
        self.current_position = 0
        self._ast = self._parse_statement()

        # Ensure the entire token stream was consumed
        remaining = self.peek_next_token()
        if remaining is not None and remaining.type != TokenType.ENDMARKER:
            raise ParserError(f"Unexpected trailing token {remaining}", remaining)

        return self._ast

    # ── Compiler (AST → Bytecode) ──────────────────────────────────

    def _compile_node(self, node: ASTNode) -> None:
        """Recursively emit bytecode for a single AST node."""
        if isinstance(node, NumberLiteral):
            self._bytecode.append(Instruction(OpCode.LOAD_CONST, node.value))

        elif isinstance(node, Identifier):
            self._bytecode.append(Instruction(OpCode.LOAD_NAME, node.name))

        elif isinstance(node, UnaryOp):
            self._compile_node(node.operand)
            opcode = OpCode.UNARY_NEG if node.op == '-' else OpCode.UNARY_POS
            self._bytecode.append(Instruction(opcode))

        elif isinstance(node, BinaryOp):
            self._compile_node(node.left)
            self._compile_node(node.right)
            opcode = _OPERATOR_TO_OPCODE.get(node.op)
            if opcode is None:
                raise CompilerError(f"Unknown binary operator {node.op!r}")
            self._bytecode.append(Instruction(opcode))

        elif isinstance(node, Assignment):
            self._compile_node(node.value)
            self._bytecode.append(Instruction(OpCode.STORE_NAME, node.target.name))

        else:
            raise CompilerError(f"Cannot compile node of type {type(node).__name__}")

    def compile_expression(self):
        # Logic to compile the parsed expression into executable code
        # This is where you would implement your compilation logic
        # import dis
        # dis.dis(self.expression)
        #         0 LOAD_CONST           2 (4)
        #         3 STORE_NAME           0 (x)
        #         6 LOAD_CONST           1 (None)
        #         9 RETURN_VALUE          
        if self._ast is None:
            raise CompilerError("No AST available — call parse_expression() first")

        self._bytecode.clear()
        self._compile_node(self._ast)
        self._bytecode.append(Instruction(OpCode.RETURN_VALUE))
        return self._bytecode

    # ── Stack-Machine Evaluator ────────────────────────────────────

    def evaluate_expression(self):
        # Logic to evaluate the compiled code and return the result
        # This is where you would implement your evaluation logic
        # result = eval(self.expression)
        # return result
        # Magic number is the value in the .pyc file , based on the version of Python.
        #import binascii
        #import importlib.util
        #version = (3350).to_bytes(2,'little') + b'\r\n' + (0).to_bytes(4,'little') + (0).to_bytes(4,'little')
        #binascii.hexlify(version)
        #b'160d0d0a
        #b=bytearray.fromhex('1B911558')
        #s=struct.unpack('=L', b)
        #time.asctime(time.localtime(s[0]))
        #Header of .pyc file is 16 bytes long, consisting of:
        # 4 bytes: Bitfield (indicating the type of .pyc file)
        # marshal — Internal Python object serialization
        # This module contains functions that can read 
        #  and write Python values in a binary format. 
        # The format is specific to Python, but independent of machine architecture issues (e.g., you can write a Python value to a file on a PC, transport the file to a Mac, and read it back there). Details of the format are undocumented on purpose; it may change between Python versions (although it rarely does).
        #import marshal
        # data = 42
        # dumped = marshal.dumps(data)
        # print(dumped)
        # print(marshal.loads(dumped))
        # Bytecode
        # Call Stack
        # Frame contains the code Object , Code Object Function , Bytecode, Global Variables and the local variables.
        # Inside the evaluator, we have the bytecode 
        #TARGET(LOAD_CONST){
        #*PyObject *value = GETITEM(consts, oparg);
        #PY_INCREF(value);
        #PUSH(value);
        #FAST_DISPATCH();
        #}
        #TARGET(BINARY_ADD)
        #{ PyObject *left = POP();
        #  PyObject *right = POP();
        #  PyObject *SUM;
        #if(PyUnicodecheckExact(left) && PyUnicodeCheckExact(right)) {
        #    sum = unicode_concatenate(left, right);
        # Unicode_concatenate consumed the ref to left 
        #}
        # else{
            # sum = PyNumber_Add(left, right);
            # Py_DECREF(left);
            #}
            #Py_DECREF(right);
            # SET_TOP(sum);
            # if (sum == NULL) {
                # goto error;
                # DISPATCH();
        # }
        # PyObject *PyEvalFrameDefault(PyFrameObject *f , int throwflag){
        # ifdef CASE_TOO_BIG:
        #       default: switch (opcode) {
        # endif
        # ...
        # }
        #}
        if not self._bytecode:
            raise EvaluatorError("No bytecode available — call compile_expression() first")

        stack: List[Any] = []
        env = self._environment

        for instr in self._bytecode:
            match instr.opcode:
                case OpCode.LOAD_CONST:
                    stack.append(instr.arg)

                case OpCode.LOAD_NAME:
                    name = instr.arg
                    if name not in env:
                        raise EvaluatorError(f"Undefined name {name!r}")
                    stack.append(env[name])

                case OpCode.STORE_NAME:
                    if not stack:
                        raise EvaluatorError("STORE_NAME on empty stack")
                    env[instr.arg] = stack[-1]  # store but leave on stack for return

                case OpCode.UNARY_NEG:
                    stack.append(-stack.pop())

                case OpCode.UNARY_POS:
                    stack.append(+stack.pop())

                case OpCode.RETURN_VALUE:
                    return stack[-1] if stack else None

                case _ if instr.opcode in _OPCODE_TO_CALLABLE:
                    right = stack.pop()
                    left = stack.pop()
                    stack.append(_OPCODE_TO_CALLABLE[instr.opcode](left, right))

                case _:
                    raise EvaluatorError(f"Unknown opcode {instr.opcode}")

        return stack[-1] if stack else None

    def execute_expression(self):
        # Logic to execute the compiled code
        # This is where you would implement your execution logic
        # exec(self.expression)
        self.tokenize()
        self.parse_expression()
        self.compile_expression()
        return self.evaluate_expression()

    # ── Introspection Helpers ──────────────────────────────────────

    def dump_tokens(self) -> str:
        """Return a human-readable listing of the token stream."""
        lines = [f"{'IDX':>4}  {'TYPE':<12}  {'VALUE':<12}  {'POS':>4}"]
        lines.append("-" * 40)
        for i, tok in enumerate(self.tokens):
            lines.append(f"{i:>4}  {tok.type.name:<12}  {tok.value!r:<12}  {tok.position:>4}")
        return "\n".join(lines)

    def dump_ast(self) -> str:
        """Return a formatted string representation of the AST."""
        if self._ast is None:
            return "<no AST>"
        return repr(self._ast)

    def dump_bytecode(self) -> str:
        """Return a disassembly-style listing of compiled bytecode."""
        lines = [f"{'OFFSET':>6}  {'OPCODE':<18}  {'ARG'}"]
        lines.append("-" * 42)
        for offset, instr in enumerate(self._bytecode):
            arg_str = repr(instr.arg) if instr.arg is not None else ""
            lines.append(f"{offset:>6}  {instr.opcode.name:<18}  {arg_str}")
        return "\n".join(lines)

    @property
    def environment(self) -> Dict[str, Any]:
        """Read-only view of the evaluator's variable bindings."""
        return dict(self._environment)


if __name__ == "__main__":
    expression = "x = 2 + 2"
    lexer = LexerExampleWithExpressionKnown(expression)
    lexer.tokenize()
    lexer.parse_expression()
    lexer.compile_expression()
    result = lexer.evaluate_expression()
    print(f"Result of the expression '{expression}': {result}")

    # ── Extended demonstration ──
    print("\n" + "=" * 60)
    print("TOKEN STREAM")
    print("=" * 60)
    print(lexer.dump_tokens())

    print("\n" + "=" * 60)
    print("ABSTRACT SYNTAX TREE")
    print("=" * 60)
    print(lexer.dump_ast())

    print("\n" + "=" * 60)
    print("BYTECODE DISASSEMBLY")
    print("=" * 60)
    print(lexer.dump_bytecode())

    print("\n" + "=" * 60)
    print("ENVIRONMENT AFTER EVALUATION")
    print("=" * 60)
    for name, val in lexer.environment.items():
        print(f"  {name} = {val}")

    # ── Additional expressions ──
    print("\n" + "=" * 60)
    print("ADDITIONAL EXPRESSIONS")
    print("=" * 60)
    test_expressions = [
        "3 + 4 * 2",
        "(3 + 4) * 2",
        "2 ** 3 ** 2",
        "10 // 3",
        "10 % 3",
        "-5 + 3",
    ]
    for expr in test_expressions:
        pipeline = LexerExampleWithExpressionKnown(expr)
        result = pipeline.execute_expression()
        print(f"  {expr:<20} = {result}")
