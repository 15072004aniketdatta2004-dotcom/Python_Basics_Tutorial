import dis
import struct
from typing import Any, List


class ComplexCalculator:
    """Performs basic arithmetic operations on complex numbers."""

    def __init__(self, real0: float, imag0: float, real1: float, imag1: float):
        self.num0 = complex(real0, imag0)
        self.num1 = complex(real1, imag1)

    def add(self) -> complex:
        return self.num0 + self.num1

    def subtract(self) -> complex:
        return self.num0 - self.num1

    def multiply(self) -> complex:
        return self.num0 * self.num1

    def divide(self) -> complex:
        if self.num1 == 0:
            raise ZeroDivisionError("Cannot divide by zero complex number.")
        return self.num0 / self.num1

    def display_operations(self) -> None:
        print(f"Addition: {self.add()}")
        print(f"Subtraction: {self.subtract()}")
        print(f"Multiplication: {self.multiply()}")
        print(f"Division: {self.divide()}")


class ListOperationDemo:
    """Demonstrates list concatenation methods and bytecode differences."""

    @staticmethod
    def array_inplace_concatenate() -> List[int]:
        x = [1, 2]
        x += [3, 4]
        return x

    @staticmethod
    def array_concatenate() -> List[int]:
        x = [1, 2]
        x = x + [3, 4]
        return x

    @staticmethod
    def show_inplace_vs_concatenate() -> None:
        print("--- In-place vs Concatenate ---")
        print("In-place (+=):", ListOperationDemo.array_inplace_concatenate())
        print("Concatenate (+):", ListOperationDemo.array_concatenate())

    @staticmethod
    def show_bytecode() -> None:
        print("\n--- Bytecode for in-place concatenation ---")

        def f():
            x = [1, 2]
            x += [3, 4]
        dis.dis(f)

    @staticmethod
    def show_mutable_behavior() -> None:
        print("\n--- Mutable behavior with += (aliases same object) ---")
        a = [1, 2]
        b = a
        a += [3, 4]
        print("a:", a)
        print("b:", b)  # b is also modified because += mutates in-place

        print("\n--- Mutable behavior with + (creates new object) ---")
        a = [1, 2]
        b = a
        a = a + [3, 4]
        print("a:", a)
        print("b:", b)  # b is unchanged because + creates a new list


class NumberComparator:
    """Demonstrates basic number comparisons and boolean operations."""

    @staticmethod
    def compare_ints(a: int, b: int) -> None:
        print(f"\n--- Integer Comparison: {a} vs {b} ---")
        diff = a - b
        if diff > 0:
            print(f"{a} is greater than {b}")
        elif diff < 0:
            print(f"{a} is less than {b}")
        else:
            print(f"{a} is equal to {b}")

    @staticmethod
    def compare_floats(c: float, d: float) -> None:
        print(f"\n--- Float Comparison: {c} vs {d} ---")
        c_bool = bool(c)
        d_bool = bool(d)

        if c > d:
            print(f"{c} is greater than {d}")
        elif c < d:
            print(f"{c} is less than {d}")
        else:
            print(f"{c} is equal to {d}")

        if c_bool ^ d_bool:
            print(f"Exactly one of {c} or {d} is non-zero")
        if not (c_bool or d_bool):
            print(f"Both {c} and {d} are zero")

        print(f"c_bool: {c_bool}, d_bool: {d_bool}")
        if c_bool and d_bool:
            print(f"Both {c} and {d} are non-zero")


class TruthinessChecker:
    """Tests truthiness and falsiness of Python data structures."""

    @staticmethod
    def check_falsy_values() -> None:
        print("\n--- Falsy Values ---")
        values = [
            None,
            "",
            [],
            (),
            {},
            set(),
            frozenset(),
            bytearray(),
            bytes(),
            range(0),
            memoryview(b""),
            complex(0, 0),
            0.0,
        ]
        names = [
            "None",
            "Empty string",
            "Empty list",
            "Empty tuple",
            "Empty dict",
            "Empty set",
            "Empty frozenset",
            "Empty bytearray",
            "Empty bytes",
            "Empty range",
            "Empty memoryview",
            "Zero complex",
            "Zero float",
        ]
        for val, name in zip(values, names):
            print(f"  {name:20s} -> bool = {bool(val)}")

    @staticmethod
    def check_truthy_values() -> None:
        print("\n--- Truthy Values ---")
        truthy_values = [
            1,
            -1,
            0.1,
            -0.1,
            "non-empty string",
            [1],
            (1,),
            {1: "a"},
            {1},
            frozenset({1}),
            bytearray(b"1"),
            bytes(b"1"),
            range(1),
            memoryview(b"1"),
            complex(1, 1),
        ]
        for value in truthy_values:
            print(f"  {str(value):30s} -> bool = {bool(value)}")


class NumberConverter:
    """Base interface for all converter implementations."""

    def convert(self, value: Any) -> Any:
        raise NotImplementedError


class FloatToBinaryConverter(NumberConverter):
    """Converts a float to its IEEE 754 single-precision binary representation."""

    def convert(self, x: float) -> str:
        if not isinstance(x, (int, float)):
            raise TypeError("Input must be a number.")
        packed = struct.pack(">f", float(x))
        bits = bin(int.from_bytes(packed, byteorder="big"))[2:]
        return bits.zfill(32)


class BinaryToFloatConverter(NumberConverter):
    """Converts a 32-bit binary string to its IEEE 754 float value."""

    def convert(self, b: str) -> float:
        if not isinstance(b, str):
            raise TypeError("Input must be a string.")
        if len(b) != 32 or not all(c in "01" for c in b):
            raise ValueError("Input must be a 32-character binary string.")
        int_value = int(b, 2)
        packed = int_value.to_bytes(4, byteorder="big")
        return struct.unpack(">f", packed)[0]


class DecimalToOctalConverter(NumberConverter):
    def convert(self, n: int) -> str:
        if not isinstance(n, int):
            raise TypeError("Input must be an integer.")
        return f"{n:o}"


class DecimalToHexConverter(NumberConverter):
    def convert(self, decimal_number: int) -> str:
        if not isinstance(decimal_number, int):
            raise TypeError("Input must be an integer.")
        return f"{decimal_number:x}"


class FloatToOctalConverter(NumberConverter):
    def __init__(self, max_fractional_digits: int = 10):
        self.max_fractional_digits = max_fractional_digits

    def convert(self, f: float) -> str:
        if not isinstance(f, (int, float)):
            raise TypeError("Input must be a number (int or float).")

        sign = "-" if f < 0 else ""
        f = abs(f)
        integer_part = int(f)
        fractional_part = f - integer_part

        octal_integer = f"{integer_part:o}"
        octal_fractional: List[str] = []

        for _ in range(self.max_fractional_digits):
            if fractional_part == 0:
                break
            fractional_part *= 8
            digit = int(fractional_part)
            octal_fractional.append(str(digit))
            fractional_part -= digit

        if octal_fractional:
            return f"{sign}{octal_integer}.{''.join(octal_fractional)}"
        return f"{sign}{octal_integer}"


class OctalToFloatConverter(NumberConverter):
    def convert(self, octal_str: str) -> float:
        if not isinstance(octal_str, str):
            raise TypeError("Input must be a string.")

        octal_str = octal_str.strip()
        if not octal_str:
            raise ValueError("Input string cannot be empty.")

        sign = 1.0
        if octal_str.startswith("-"):
            sign = -1.0
            octal_str = octal_str[1:]
        elif octal_str.startswith("+"):
            octal_str = octal_str[1:]

        if "." in octal_str:
            integer_part_str, fractional_part_str = octal_str.split(".", 1)
        else:
            integer_part_str, fractional_part_str = octal_str, ""

        integer_part = int(integer_part_str, 8) if integer_part_str else 0
        fractional_part = 0.0

        for i, digit in enumerate(fractional_part_str):
            fractional_part += int(digit, 8) * (8 ** -(i + 1))

        return sign * (integer_part + fractional_part)


class HexToDecimalConverter(NumberConverter):
    def convert(self, hex_str: str) -> int:
        if not isinstance(hex_str, str):
            raise TypeError("Input must be a string.")
        return int(hex_str, 16)


class ConversionService:
    """Registry that dispatches conversion requests to registered converters."""

    def __init__(self):
        self.converters: dict[str, NumberConverter] = {}

    def register_converter(self, name: str, converter: NumberConverter) -> None:
        self.converters[name] = converter

    def convert(self, name: str, value: Any) -> Any:
        if name not in self.converters:
            raise ValueError(f"Unknown converter: {name}")
        return self.converters[name].convert(value)


class LogicalOperatorDemo:
    """Demonstrates logical operators with provided boolean values."""

    @staticmethod
    def run(op1: bool, op2: bool) -> None:
        print(f"\n--- Logical Operators: op1={op1}, op2={op2} ---")
        if op1 and op2:
            print(f"  Both {op1} and {op2} are True")
        if op1 or op2:
            print(f"  At least one of {op1} or {op2} is True")
        if not op1:
            print(f"  op1 ({op1}) is False")
        if not op2:
            print(f"  op2 ({op2}) is False")
        if op1 ^ op2:
            print(f"  Exactly one of {op1} or {op2} is True")


class BitwiseOperatorDemo:
    """Demonstrates bitwise operations on integers."""

    @staticmethod
    def run(a: int, b: int) -> None:
        print(f"\n--- Bitwise Operations: a={a}, b={b} ---")
        print(f"  AND  (a & b) : {a & b}")
        print(f"  OR   (a | b) : {a | b}")
        print(f"  XOR  (a ^ b) : {a ^ b}")
        print(f"  NOT  (~a)    : {~a}")
        print(f"  NOT  (~b)    : {~b}")
        print(f"  LSH  (a << 2): {a << 2}")
        print(f"  RSH  (a >> 2): {a >> 2}")
        print(f"  XNOR ~(a^b) : {~(a ^ b)}")

    @staticmethod
    def run_conditional_example() -> None:
        """Shows how short-circuit evaluation and precedence affect conditionals."""
        print("\n--- Conditional / Short-circuit Examples ---")
        b = 1
        c = 1
        d = 0

        # 0 is falsy, so `0 and ...` short-circuits to 0 → False
        if 0 and (0 == 0):
            print("1 Python 3.12.12")

        # b=1 is truthy, so `1 or ...` short-circuits to 1 → True
        if b or (b - 1 == 0):
            print("2 Python 3.12.12")

        # c=1 is truthy, same logic
        if c or (c - 1 == 0):
            print("3 Python 3.12.12")

        # d=0 is falsy, then (d + 1 == 0) → (1 == 0) → False
        if d or (d + 1 == 0):
            print("4 Python 3.12.12")


class Operators:
    """Demonstrates list operations."""

    def __init__(self, list1: List[int], list2: List[int]):
        self.list1 = list1
        self.list2 = list2

    def concatenate_lists(self) -> List[int]:
        self.list2 += self.list1
        return self.list2


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def _parse_int_list(prompt: str) -> List[int]:
    """Helper: reads a comma-separated list of integers from the user."""
    raw = input(prompt)
    return [int(x.strip()) for x in raw.split(",")]


def main() -> None:
    # --- List operation demos (fixed pedagogical examples) ---
    ListOperationDemo.show_inplace_vs_concatenate()
    ListOperationDemo.show_bytecode()
    ListOperationDemo.show_mutable_behavior()

    # --- Integer comparison (user input) ---
    print("\n--- Integer Comparison ---")
    int_a = int(input("Enter first integer: "))
    int_b = int(input("Enter second integer: "))
    NumberComparator.compare_ints(int_a, int_b)

    # --- Float comparison (user input) ---
    print("\n--- Float Comparison ---")
    float_c = float(input("Enter first float: "))
    float_d = float(input("Enter second float: "))
    NumberComparator.compare_floats(float_c, float_d)

    # --- Truthiness (fixed pedagogical examples) ---
    TruthinessChecker.check_falsy_values()
    TruthinessChecker.check_truthy_values()

    # --- Complex arithmetic (user input) ---
    print("\n--- Complex Calculator ---")
    real0 = float(input("Enter real part of first complex number: "))
    imag0 = float(input("Enter imaginary part of first complex number: "))
    real1 = float(input("Enter real part of second complex number: "))
    imag1 = float(input("Enter imaginary part of second complex number: "))
    calc = ComplexCalculator(real0, imag0, real1, imag1)
    calc.display_operations()

    # --- Conversion service (user input for every conversion) ---
    service = ConversionService()
    service.register_converter("float_to_binary", FloatToBinaryConverter())
    service.register_converter("binary_to_float", BinaryToFloatConverter())
    service.register_converter("decimal_to_octal", DecimalToOctalConverter())
    service.register_converter("decimal_to_hex", DecimalToHexConverter())
    service.register_converter("float_to_octal", FloatToOctalConverter())
    service.register_converter("octal_to_float", OctalToFloatConverter())
    service.register_converter("hex_to_decimal", HexToDecimalConverter())

    print("\n--- Number Conversions ---")

    ftb = float(input("Enter a float to convert to binary (e.g. 3.5): "))
    print("  Result:", service.convert("float_to_binary", ftb))

    btf = input("Enter a 32-bit binary string to convert to float: ")
    print("  Result:", service.convert("binary_to_float", btf))

    dto = int(input("Enter a decimal integer to convert to octal (e.g. 65): "))
    print("  Result:", service.convert("decimal_to_octal", dto))

    dth = int(input("Enter a decimal integer to convert to hex (e.g. 255): "))
    print("  Result:", service.convert("decimal_to_hex", dth))

    fto = float(input("Enter a float to convert to octal (e.g. 12.5): "))
    print("  Result:", service.convert("float_to_octal", fto))

    otf = input("Enter an octal string to convert to float (e.g. 14.4): ")
    print("  Result:", service.convert("octal_to_float", otf))

    htd = input("Enter a hex string to convert to decimal (e.g. 1F): ")
    print("  Result:", service.convert("hex_to_decimal", htd))

    # --- Logical operators (user input) ---
    print("\n--- Logical Operators ---")
    op1 = input("Enter a boolean for op1 (True/False): ").strip().lower() == "true"
    op2 = input("Enter a boolean for op2 (True/False): ").strip().lower() == "true"
    LogicalOperatorDemo.run(op1, op2)

    # --- Bitwise operators (user input) ---
    print("\n--- Bitwise Operators ---")
    bit_a = int(input("Enter first integer for bitwise operations: "))
    bit_b = int(input("Enter second integer for bitwise operations: "))
    BitwiseOperatorDemo.run(bit_a, bit_b)
    BitwiseOperatorDemo.run_conditional_example()

    # --- List concatenation via Operators class (user input) ---
    print("\n--- Operators list concatenation ---")
    list1 = _parse_int_list("Enter list1 as comma-separated ints (e.g. 10,20): ")
    list2 = _parse_int_list("Enter list2 as comma-separated ints (e.g. 30,40): ")
    demo = Operators(list1, list2)
    print("Concatenated list:", demo.concatenate_lists())


if __name__ == "__main__":
    main()
