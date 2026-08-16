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
    def understandingrange(self):
        r1 = range(10)
        r2 = range(10)
        print(r1 == r2)  # True  (Value equality check succeeds in O(1))
        print(r1 is r2)  # False (Distinct memory addresses on the heap)
        print(id(r1) != id(r2))  # True
        print(id(r1),id(r2))  # DIFFERENT memory addresses  
    def  stringsAnalysis(self):
        pass        
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