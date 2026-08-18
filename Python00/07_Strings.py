import sys
import ctypes

class StringsOverview:
    def __init__(self,input_str):
        self.input_str = input_str
    
    def ASCIIValueGetter(self):
        for char in self.input_str:
            print(ord(char))
    def charactersPrinter(self):
        for char0 in self.input_str:
            print(char0)
        print(len(self.input_str))
    def stack_memory_pyframe_of_Strings_Analysis(self):
        s = self.input_str

        print("=" * 60)
        print("  STACK / FRAME MEMORY ANALYSIS FOR STRINGS")
        print("=" * 60)

        # 1. Object identity and memory address
        print("\n--- 1. Object Identity (id = memory address in CPython) ---")
        print(f"  Variable 'self.input_str' -> id: {id(self.input_str)}")
        print(f"  Variable 's' (alias)      -> id: {id(s)}")
        print(f"  Same object? {s is self.input_str}")  # True — both point to same object

        # 2. Memory size of the string object
        print("\n--- 2. Memory Size (sys.getsizeof) ---")
        print(f"  String value : '{s}'")
        print(f"  Length (chars): {len(s)}")
        print(f"  Size in bytes : {sys.getsizeof(s)} bytes")
        print(f"  (Includes PyObject header + internal char buffer)")

        # 3. Reference count — how many names point to this object
        print("\n--- 3. Reference Count (sys.getrefcount) ---")
        refcount = sys.getrefcount(s)  # Note: getrefcount adds 1 temporary ref
        print(f"  sys.getrefcount(s) = {refcount}")
        print(f"  Actual refs ~ {refcount - 1} (getrefcount itself adds 1)")

        # 4. String interning demonstration
        print("\n--- 4. String Interning ---")
        a = "hello"
        b = "hello"
        print(f"  a = 'hello' -> id: {id(a)}")
        print(f"  b = 'hello' -> id: {id(b)}")
        print(f"  a is b? {a is b}")  # True — CPython interns short literals
        c = "hello world!!"
        d = "hello world!!"
        print(f"  c = 'hello world!!' -> id: {id(c)}")
        print(f"  d = 'hello world!!' -> id: {id(d)}")
        print(f"  c is d? {c is d}")  # May be False — not always interned

        # 5. Slicing creates NEW objects
        print("\n--- 5. Slicing Creates New Objects ---")
        sliced = s[0:3]
        print(f"  Original s      -> id: {id(s)}")
        print(f"  Slice s[0:3]    -> id: {id(sliced)}, value: '{sliced}'")
        print(f"  Same object? {sliced is s}")  # False — new string created
        full_slice = s[:]
        print(f"  Full slice s[:] -> id: {id(full_slice)}")
        print(f"  Same as s?  {full_slice is s}")  # True — CPython optimizes full slice

        # 6. Concatenation creates NEW objects
        print("\n--- 6. Concatenation Creates New Objects ---")
        s1 = "Py"
        s2 = "thon"
        s3 = s1 + s2
        literal = "Python"
        print(f"  s1 = 'Py'       -> id: {id(s1)}")
        print(f"  s2 = 'thon'     -> id: {id(s2)}")
        print(f"  s3 = s1 + s2    -> id: {id(s3)}, value: '{s3}'")
        print(f"  s3 == literal? {s3 == literal} (equal value), s3 is literal? {s3 is literal} (same obj)")

        # 7. Immutability proof
        print("\n--- 7. Immutability Proof ---")
        print(f"  id(s) BEFORE any operation: {id(s)}")
        s_new = s + "!"
        print(f"  s_new = s + '!'")
        print(f"  id(s)     AFTER: {id(s)}     (unchanged — original intact)")
        print(f"  id(s_new) AFTER: {id(s_new)} (new object created)")

        # 8. Per-character memory layout
        print("\n--- 8. Per-Character Object IDs (each char is its own str) ---")
        for i, ch in enumerate(s[:min(len(s), 10)]):  # limit to first 10 chars
            print(f"  s[{i}] = '{ch}' -> id: {id(ch)}, size: {sys.getsizeof(ch)} bytes")

        print("\n" + "=" * 60)
    def stringConcatenation(self):
        s1=''
        s2='Python 3.14.2'
        print(id(s1+s2))
        print(id(s2+s1))
        print((s1+s2)==(s2+s1))
        s1='STELLA'
        s2='MEGAN'
        if((s1+s2)==(s2+s1)):
            print("+ is commutative")
        else:
            print("+ is not commutative")
        print(s1+" "+ s2)

    def stringRepeatition(self,str1:str):
        str2 = str1 * 3
        print(str2)
        if ((3*str1)==(str1*3)):
            print("* is commutative")
        else:
            print("* is not commutative")
    def inNotInOperator(self):
        s1 = "Python 3.14.2"# Haystack Buffer #Boyer Moore Horspool
        s2 = "Python" # Needle Buffer
        s3 = "Java"
        print(s2 in s1)
        print(s3 in s1)
        print(s2 not in s1)
        print(s3 not in s1)
    def stringFormatting(self):
        print(f"Hello {self.input_str}")
        print("Hello %s" % self.input_str)
        print("Hello {}".format(self.input_str))
    def comparingStrings(self):
        print("Python"<"Python 3.14.2")
        print("Python"<"python")
        print(ord("P"))
        print(ord("p"))
        print("p"<"P")
        print("Python"<"Pytorch")
    def slicingStrings(self,input_str1:str):
        print(type(input_str1))
        print(input_str1[0])
        print(input_str1[-1])
        print(input_str1[2:4])
        print(input_str1[2::3])
        print(input_str1[:3:1])
        print(input_str[::2])
        print(input_str1[3::-1])
        print(input_str1[::-1])
        print(input_str[-6:-3:1])
        str2:str="Hello, World!"
        print(str2[3:1]) #Empty Slice
        place="Williamstown"
        print(place[0:-4:1]) #William
        print(place[0:8:1]) #Williams
        print(place[0:8:-1]) #Enpty slice
        a:int=[6,5,4,3,2,1,0]
        b:str="success"
        c:str=b[a[-3]]+b[::4]
        d:int=a[1]*a[2]*a[-3]*a[4//2]
        x=str(c)+str(d)
        print(f"type of x: {type(x)}")
        print(f"x= {x}")
        reversed_string:str=self.input_str[::-1]
        print(reversed_string)
        temp:str=""
        # range(start= len(self.input_str)-1, stop=-1, step=-1) as stop is always exclusive so the range is till 0
        for i in range(len(self.input_str)-1,-1,-1):
            temp+=self.input_str[i] 
        print(temp)  
    def understandingrange(self):
        r1 = range(10)
        r2 = range(10)
        print(r1 == r2)  # True  (Value equality check succeeds in O(1))
        print(r1 is r2)  # False (Distinct memory addresses on the heap)
        print(id(r1) != id(r2))  # True
        print(id(r1),id(r2))  # DIFFERENT memory addresses
        r3=range(5,-1,-1)
        print(list(r3)) #[len(input_str)-1,..........,5,4,3,2,1,0]
    def  stringsAnalysis(self):
        newstr:str=input("Enter a new string: ")
        print(id(newstr),id(self.input_str))
        print(newstr is self.input_str )
        self.input_str=sys.intern(self.input_str)
        print(id(newstr),id(self.input_str))
        print(newstr is self.input_str ) 
    class Demo:
        input_str = "STRING"  # Class-level literal (compiled into module co_consts)
        def LetSee(self):
            newstr = "STRING"  # Function-level literal (shares same interned pointer)
            print(newstr is self.input_str)  # True
        # def __init__(self,input_str1:str):
        #     self.input_str1=input_str1
    demo = Demo()    
    demo.LetSee()
    def whitespacesStripping(self, input_str1:str):
        stripped_string=input_str1.strip()
        right_stripped_string=input_str1.rstrip()
        left_stripped_string=input_str1.lstrip()
        print(f'stripped_string: {stripped_string}')
        print(f'right_stripped_string: {right_stripped_string}')
        print(f'left_stripped_string: {left_stripped_string}')
        print(f'id(input_str1): {id(input_str1)}')
        print(f'id(stripped_string): {id(stripped_string)}')
        print(f'id(right_stripped_string): {id(right_stripped_string)}')
        print(f'id(left_stripped_string): {id(left_stripped_string)}')
        print(f'stripped_string is input_str1: {stripped_string is input_str1}')
        print(f'right_stripped_string is input_str1: {right_stripped_string is input_str1}')
        print(f'left_stripped_string is input_str1: {left_stripped_string is input_str1}')
    def ImmutableObjectSequenceTypesString(self, input_str1:str):
        """
        Demonstrates the existence of:
          1. Stack PyFrame object  — the live frame on the C call stack
          2. PyObject references   — raw CPython object header (ob_refcnt, ob_type)
          3. Heap allocation       — every string mutation creates a NEW object on the heap

        Strings are IMMUTABLE SEQUENCE types: they support indexing, slicing,
        iteration, len(), 'in', but NEVER in-place modification.
        """
        import sys
        import ctypes

        banner = lambda title: print(f"\n{'=' * 70}\n  {title}\n{'=' * 70}")

        # ─────────────────────────────────────────────────────────────
        #  SECTION 1 : STACK — PyFrame Object
        # ─────────────────────────────────────────────────────────────
        banner("SECTION 1 : STACK — PyFrame Object (sys._getframe)")

        frame = sys._getframe(0)   # current executing frame

        print(f"\n  ┌─ Frame Object ─────────────────────────────────────────")
        print(f"  │  type(frame)        : {type(frame)}")
        print(f"  │  id(frame)          : {id(frame)}  (frame's own heap address)")
        print(f"  │  frame.f_code.co_name      : {frame.f_code.co_name}")
        print(f"  │  frame.f_code.co_filename  : {frame.f_code.co_filename}")
        print(f"  │  frame.f_code.co_varnames  : {frame.f_code.co_varnames}")
        print(f"  │  frame.f_lineno            : {frame.f_lineno}")
        print(f"  │  frame.f_locals keys       : {list(frame.f_locals.keys())}")
        print(f"  └──────────────────────────────────────────────────────────")

        # Show the CALLER's frame to illustrate the frame chain (stack)
        caller_frame = frame.f_back
        if caller_frame:
            print(f"\n  ┌─ Caller Frame (f_back) ────────────────────────────────")
            print(f"  │  caller.f_code.co_name     : {caller_frame.f_code.co_name}")
            print(f"  │  caller.f_lineno            : {caller_frame.f_lineno}")
            print(f"  │  id(caller_frame)           : {id(caller_frame)}")
            print(f"  └──────────────────────────────────────────────────────────")

        # Walk the full frame chain
        print("\n  Full frame chain (stack → bottom):")
        f = frame
        depth = 0
        while f is not None:
            print(f"    [{depth}] {f.f_code.co_name:30s}  line {f.f_lineno}  id={id(f)}")
            f = f.f_back
            depth += 1

        # Local variables on THIS frame — these are REFERENCES (pointers)
        # stored on the stack frame, pointing to heap-allocated PyObjects
        print(f"\n  ► 'input_str1' lives as a local variable reference on THIS frame.")
        print(f"    Stack ref name : 'input_str1'")
        print(f"    Points to heap : id = {id(input_str1)}")
        print(f"    Value          : '{input_str1}'")

        # ─────────────────────────────────────────────────────────────
        #  SECTION 2 : PyObject — CPython Object Header on the Heap
        # ─────────────────────────────────────────────────────────────
        banner("SECTION 2 : PyObject — CPython Object Header via ctypes")

        print("""
  In CPython, every Python object is a C struct on the heap:

      typedef struct {
          Py_ssize_t  ob_refcnt;   // reference count
          PyTypeObject *ob_type;   // pointer to type object
          // ... type-specific data follows ...
      } PyObject;

  id(obj) returns the memory address of this struct.
        """)

        # Read the raw ob_refcnt from the PyObject header using ctypes
        addr = id(input_str1)
        # ob_refcnt is the first field — a Py_ssize_t (platform-sized signed int)
        raw_refcnt = ctypes.c_ssize_t.from_address(addr).value
        # ob_type pointer is right after ob_refcnt
        type_ptr = ctypes.c_void_p.from_address(addr + ctypes.sizeof(ctypes.c_ssize_t)).value

        print(f"  String value         : '{input_str1}'")
        print(f"  id(input_str1)       : {addr}  (= PyObject* address on heap)")
        print(f"  ob_refcnt (raw)      : {raw_refcnt}")
        print(f"  sys.getrefcount()    : {sys.getrefcount(input_str1)}  (adds +1 temporary)")
        print(f"  ob_type ptr          : {hex(type_ptr) if type_ptr else 'N/A'}")
        print(f"  id(type(input_str1)) : {id(type(input_str1))}  (should match ob_type)")
        print(f"  type(input_str1)     : {type(input_str1)}")
        print(f"  sys.getsizeof()      : {sys.getsizeof(input_str1)} bytes")

        # Show that each character (when extracted) is ALSO a PyObject on heap
        print(f"\n  ► Each character extracted from the string is its own PyObject:")
        for i in range(min(len(input_str1), 8)):
            ch = input_str1[i]
            ch_addr = id(ch)
            ch_refcnt = ctypes.c_ssize_t.from_address(ch_addr).value
            print(f"    input_str1[{i}] = '{ch}'  "
                  f"id={ch_addr}  ob_refcnt={ch_refcnt}  "
                  f"size={sys.getsizeof(ch)}B")

        # ─────────────────────────────────────────────────────────────
        #  SECTION 3 : HEAP — Immutability Proof (new objects each time)
        # ─────────────────────────────────────────────────────────────
        banner("SECTION 3 : HEAP — Immutability Creates New PyObjects")

        original_id = id(input_str1)
        print(f"\n  Original string : '{input_str1}'")
        print(f"  Original id     : {original_id}")
        print(f"  Original size   : {sys.getsizeof(input_str1)} bytes\n")

        # Each operation below creates a NEW string on the heap
        operations = {
            "concatenation  (+)":   input_str1 + "!",
            "repetition     (*)":   input_str1 * 2,
            "slice          [1:]":  input_str1[1:],
            "upper()":              input_str1.upper(),
            "lower()":              input_str1.lower(),
            "replace('a','@')":     input_str1.replace('a', '@'),
            "strip()":              input_str1.strip(),
            "join (reversed)":      ''.join(reversed(input_str1)),
            "full slice     [:]":   input_str1[:],      # optimised: may reuse!
        }

        print(f"  {'Operation':<25s} {'Value':<25s} {'Heap id':<20s} {'Same obj?':<10s} {'Size':>6s}")
        print(f"  {'─'*25} {'─'*25} {'─'*20} {'─'*10} {'─'*6}")

        for desc, result in operations.items():
            same = "YES ✓" if result is input_str1 else "NO ✗"
            print(f"  {desc:<25s} {repr(result):<25s} {id(result):<20d} {same:<10s} {sys.getsizeof(result):>5d}B")

        # Prove the ORIGINAL is untouched
        print(f"\n  ► After ALL operations:")
        print(f"    id(input_str1) is still : {id(input_str1)}")
        print(f"    Value is still          : '{input_str1}'")
        print(f"    Unchanged?              : {id(input_str1) == original_id}  ✓ IMMUTABLE")

        # ─────────────────────────────────────────────────────────────
        #  SECTION 4 : Sequence Protocol — Strings as Sequences
        # ─────────────────────────────────────────────────────────────
        banner("SECTION 4 : Sequence Type Protocol (str is a Sequence)")

        print(f"\n  str supports the SEQUENCE protocol (indexing, slicing, iteration):")
        print(f"    len(input_str1)          = {len(input_str1)}")
        print(f"    input_str1[0]            = '{input_str1[0]}'")
        print(f"    input_str1[-1]           = '{input_str1[-1]}'")
        print(f"    input_str1[1:4]          = '{input_str1[1:4]}'")
        print(f"    'a' in input_str1        = {'a' in input_str1}")
        print(f"    input_str1.index('{input_str1[0]}') = {input_str1.index(input_str1[0])}")
        print(f"    input_str1.count('{input_str1[0]}') = {input_str1.count(input_str1[0])}")

        # Attempting mutation raises TypeError — proof of immutability
        print(f"\n  ► Attempting in-place mutation (input_str1[0] = 'X'):")
        try:
            input_str1[0] = 'X'  # type: ignore
        except TypeError as e:
            print(f"    TypeError: {e}")
            print(f"    ✓ Strings are IMMUTABLE — cannot assign to index")

        # ─────────────────────────────────────────────────────────────
        #  SECTION 5 : Reference Counting & Interning on the Heap
        # ─────────────────────────────────────────────────────────────
        banner("SECTION 5 : Reference Counting & String Interning on Heap")

        # Interning example
        x = "hello"
        y = "hello"
        z = sys.intern("hel" + "lo")  # Force intern a dynamically built string

        print(f"\n  x = 'hello'        id={id(x)}")
        print(f"  y = 'hello'        id={id(y)}")
        print(f"  z = intern('hel'+'lo') id={id(z)}")
        print(f"  x is y? {x is y}   (compile-time literals share ONE heap object)")
        print(f"  x is z? {x is z}   (intern forces reuse of the same heap object)")
        print(f"  refcount of x = {sys.getrefcount(x)} (many refs: interned + locals + getrefcount)")

        # Non-interned dynamic string
        dynamic = input_str1 + " " + input_str1
        print(f"\n  dynamic = input_str1 + ' ' + input_str1")
        print(f"  dynamic value   : '{dynamic}'")
        print(f"  id(dynamic)     : {id(dynamic)}  (new heap allocation)")
        print(f"  refcount        : {sys.getrefcount(dynamic)}")

        print(f"\n{'=' * 70}")
        print(f"  SUMMARY")
        print(f"{'=' * 70}")
        print(f"""
  • STACK (PyFrame):  Every function call creates a PyFrameObject on the
    C stack. Local variable NAMES live here as references (pointers).

  • PyObject (Heap):  Every Python object — including every string — is a
    PyObject struct allocated on the HEAP. The struct starts with
    ob_refcnt and ob_type, followed by type-specific data.

  • IMMUTABLE:  str is a SEQUENCE type that supports indexing, slicing,
    and iteration, but NEVER in-place mutation. Every "modification"
    allocates a NEW PyObject on the heap; the original is unchanged.

  • INTERNING:  CPython may intern short string literals so multiple
    names share the SAME heap object (same id), saving memory.
        """)
    def Repetitions(self,s:str):
#'''You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.
# Input
# The only input line contains a string of n characters.
# Output
# Print one integer: the length of the longest repetition.
# Constraints
# 1 \le n \le 10^6
# Example
# Input:
# ATTCGGGA
# Output:
# 3'''
             length=len(s)
             max_frequency:int=0
             for i in range(length):
                frequency=s.count(s[i])
                #count=1
                #for j in range(1,len(s)):
                #     if s[j] == s[j-1]:
                #          count+=1
                #     else:
                #          break
                if frequency>max_frequency:
                    max_frequency=frequency
             return max_frequency

if __name__=="__main__":
    input_str = input("Enter a string: ")
    s = StringsOverview(input_str)
    s.ASCIIValueGetter()
    s.charactersPrinter()
    s.stack_memory_pyframe_of_Strings_Analysis()
    print(isinstance(input_str,str))    
    s.stringConcatenation()
    s.stringRepeatition(input_str)
    s.inNotInOperator()
    s.stringFormatting()
    s.comparingStrings()
    s.slicingStrings(input_str)
    s.understandingrange()
    s.stringsAnalysis()
    s.Demo().LetSee()
    s.whitespacesStripping(input_str)
    s.ImmutableObjectSequenceTypesString(input_str)
    input_DNA_sequence = input("The DNA sequence is:")
    print(s.Repetitions(input_DNA_sequence))