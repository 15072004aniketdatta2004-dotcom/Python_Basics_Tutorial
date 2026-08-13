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

if __name__=="__main__":
    input_str = input("Enter a string: ")
    s = StringsOverview(input_str)
    s.ASCIIValueGetter()
    s.charactersPrinter()
    s.stack_memory_pyframe_of_Strings_Analysis()
    print(input_str[0])
    print(input_str[-1])
    print(input_str[2:4])
    print(input_str[2::3])
    print(input_str[:3:1])
    print(input_str[::2])
    print(isinstance(input_str,str))    