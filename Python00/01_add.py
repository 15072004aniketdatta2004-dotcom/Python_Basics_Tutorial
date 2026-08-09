import math

def add(a:float, b:float) -> float:
    return a + b

def subtract(a:float, b:float) -> float:
    return a - b

def multiply(a:float, b:float) -> float:
    return a * b

def divide(a:float, b:float) -> float:
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b

def power(a:float, b:float) -> float:
    return math.pow(a, b)
def modulo(a:float, b:float) -> float:
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a % b
def sqrt(a:float) -> float:
    return math.sqrt(a)
def factorial(n:int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(n)
import inspect
import gc
import sys

def print_object_metadata(obj, name="obj"):
    print("=" * 60)
    print(f"Object: {name}")
    print("=" * 60)

    print(f"Type: {type(obj)}")
    print(f"Type name: {type(obj).__name__}")
    print(f"ID (memory address): {id(obj)}")
    print(f"Hex ID: {hex(id(obj))}")
    print(f"Size (sys.getsizeof): {sys.getsizeof(obj)} bytes")

    if hasattr(obj, "__module__"):
        print(f"Module: {obj.__module__}")
    else:
        print("Module: (no __module__)")

    if inspect.isclass(obj):
        print("Is class: True")
        print(f"Base classes: {obj.__bases__}")
        print(f"Class module: {obj.__module__}")
    else:
        print("Is class: False")

    if inspect.isfunction(obj) or inspect.ismethod(obj):
        print("Is function/method: True")
        print(f"Function name: {obj.__name__}")
        print(f"Qualified name: {getattr(obj, '__qualname__', 'N/A')}")
        print(f"Default arguments: {inspect.signature(obj)}")
    else:
        print("Is function/method: False")


    print(f"Callable: {callable(obj)}")


    print(f"Repr: {repr(obj)}")
    print(f"Str: {str(obj)}")


    print("\nAttributes (dir):")
    for attr in dir(obj):

        if not attr.startswith("__"):
            try:
                value = getattr(obj, attr)
                print(f"  {attr}: {repr(value)}")
            except Exception as e:
                print(f"  {attr}: <error: {e}>")


    specials = [
        "__getitem__", "__setitem__", "__delitem__",
        "__iter__", "__next__", "__len__",
        "__enter__", "__exit__",
        "__call__", "__getattr__", "__setattr__",
    ]
    print("\nSpecial methods present:")
    for spec in specials:
        if hasattr(obj, spec):
            print(f"  {spec}: YES")
        else:
            print(f"  {spec}: NO")

    if gc.is_tracked(obj):
        print("GC tracked: True")
    else:
        print("GC tracked: False")

    
    if hasattr(sys, "getrefcount"):
        # getrefcount 
        refcount = sys.getrefcount(obj) - 1
        print(f"Reference count (approx): {refcount}")
    else:
        print("Reference count: (not available in this implementation)")

    print()
import inspect
import sys
import gc

def print_pytype_metadata(typ, name="type"):
    if not isinstance(typ, type):
        print(f"Error: {name} is not a type object (got {type(typ)})")
        return

    print("=" * 60)
    print(f"PyTypeObject (Python type): {name}")
    print("=" * 60)

    print(f"Type: {type(typ)}")
    print(f"Type name: {typ.__name__}")
    print(f"Qualified name: {getattr(typ, '__qualname__', 'N/A')}")
    print(f"Module: {getattr(typ, '__module__', 'N/A')}")
    print(f"ID (memory address): {id(typ)}")
    print(f"Hex ID: {hex(id(typ))}")
    print(f"Size (sys.getsizeof): {sys.getsizeof(typ)} bytes")

    print(f"MRO: {typ.__mro__}")

    print(f"Bases: {typ.__bases__}")

    print("\nClass __dict__ (attributes):")
    for attr, value in typ.__dict__.items():
        print(f"  {attr}: {repr(value)}")

    specials = [
        "__new__", "__init__", "__del__",
        "__getattribute__", "__getattr__", "__setattr__", "__delattr__",
        "__repr__", "__str__", "__bytes__", "__format__",
        "__lt__", "__le__", "__eq__", "__ne__", "__gt__", "__ge__",
        "__hash__", "__bool__",
        "__getitem__", "__setitem__", "__delitem__", "__len__", "__contains__",
        "__iter__", "__next__",
        "__call__", "__enter__", "__exit__",
        "__get__", "__set__", "__delete__",  # descriptor methods
        "__prepare__", "__instancecheck__", "__subclasscheck__",
    ]
    print("\nSpecial methods present:")
    for spec in specials:
        if hasattr(typ, spec):
            print(f"  {spec}: YES")
        else:
            print(f"  {spec}: NO")

    if hasattr(typ, "__get__"):
        print("Is descriptor: True")
    else:
        print("Is descriptor: False")

    if hasattr(typ, "__abstractmethods__"):
        abstracts = typ.__abstractmethods__
        print(f"Abstract methods: {abstracts}")
    else:
        print("Abstract methods: (not an ABC)")

    print(f"Subclasses: {typ.__subclasses__()}")

    try:
        if typ.__name__ not in ("type", "object"):  # 無限再帰を避ける
            instance = typ()
            print(f"Can instantiate (no args): True -> {repr(instance)}")
        else:
            print("Can instantiate (no args): (skipped for meta-types)")
    except Exception as e:
        print(f"Can instantiate (no args): False ({e})")

    if gc.is_tracked(typ):
        print("GC tracked: True")
    else:
        print("GC tracked: False")

    if hasattr(sys, "getrefcount"):
        refcount = sys.getrefcount(typ) - 1
        print(f"Reference count (approx): {refcount}")
    else:
        print("Reference count: (not available in this implementation)")

    c_fields_mapping = {
        "__name__": "tp_name",
        "__basicsize__": "tp_basicsize",
        "__itemsize__": "tp_itemsize",
        "__flags__": "tp_flags",
        "__doc__": "tp_doc",
        "__weakrefoffset__": "tp_weaklistoffset",
        "__base__": "tp_base",
        "__dictoffset__": "tp_dictoffset",
    }
    print("\nC-level PyTypeObject fields (approximate mapping):")
    for py_attr, c_field in c_fields_mapping.items():
        if hasattr(typ, py_attr):
            value = getattr(typ, py_attr)
            print(f"  {c_field} (~{py_attr}): {repr(value)}")
        else:
            print(f"  {c_field} (~{py_attr}): <not available>")

    print()
def main() -> None:
    msg: str = str(input("Enter a message: "))
    x: float = float(input("Enter a number: "))
    y: float = float(input("Enter another number: "))
    print(msg)
    print("%f" % add(x, y))
    print("%f" % subtract(x, y))
    print("%f" % multiply(x, y))
    print("%f" % divide(x, y))
    print("%f" % power(x, y))
    print("%f" % sqrt(x))
    print("%f" % modulo(x, y))
    print(factorial(int(x)))
    # import addressof and c_int modules 
    # from ctypes module
    from ctypes import c_int, addressof
    # get memory address of variable
    x0:int = 10
    print(f'value of x at time instant t1 : {x0}')
    print(f'address of x at time instant t1 : {addressof(c_int(x0))}')
    x0:int = 20
    print(f'value of x at time instant t2 : {x0}')
    print(f'address of x at time instant t2 : {addressof(c_int(x0))}')
    x0:int = 10+20
    print(f'value of x at time instant t3 : {x0}')
    print(f'address of x at time instant t3 : {addressof(c_int(x0))}')
    # get object id of variable
    x1: str = 'Python 3.24.0'
    print(hex(id(x1)))
    y1: str = 'Python 3.24.0'
    print(hex(id(y1)))
    z1: str = 'Python 3.24.2'
    print(hex(id(z1)))
    # num_1: int = 10
    # num_1=3.1428571428571428571428571428571 #bad practice
    # print(f'value of num_1 : {num_1}')
    num_1: int = 10
    print(f'num_1 is object of class {type(num_1).__name__}')
    num_1=10.0
    print(f'num_1 is object of class {type(num_1).__name__}(Dynamic Typing)')
    print_object_metadata(num_1,"num_1")
    print_pytype_metadata(type(num_1),"num_1")
    num_2: int = 17
    num_2:int =int(5.3)
    print(num_2)
    ##Naming a variable
    var_A = 11
    print(id(var_A))
    var_B = var_A
    print(id(var_B))
    var_A = 42
    print(id(var_A))
    print(id(var_B))
    print(var_B)
    # Variables are case-Sensitive
    username: str = input("Enter your username: ")
    print(f"Hello, {username}!")
    USERNAME: str = input("Enter your username: ")
    print(f"Hello, {username}:)")
    print(f"Hello, {USERNAME}?")
    #Assignment operator
    x:float=0.6
    print(f'value of x : {x}')
    print(f'object id of x : {id(x)}')
    x:float=3.9*x*(1-x)
    print(f'value of x after assignment to expression containing x\'s last value: {x}')
    print(f'object id of x after assignment to expression containing x\'s last value: {id(x)}')
    weightInKg:float=float(input("Enter weight in kg: "))
    # float for floating point number
    weightInPounds:float=weightInKg*2.20462
    print(f'weight in pounds : {weightInPounds}')
    #int for Integers number
    NumberOfStudents:int=int(input("Enter number of students: "))
    print(f'Number of students : {NumberOfStudents}')
    # Immutable Data Types: int, float, bool, str, tuple, frozenset,Bytes
    userName: str = "Anonymous_User" # Here the object in the string pool is never modified, instead a new object is created in the string pool and the variable userName is assigned to that new object.
    print("object id of userName : ",id(userName))
    userName: str = "Aniket Datta" # Here the reference of the variable userName is changed to a new object in the string pool, and the previous object is coolected by garbage collector.
    print("object id of userName : ",id(userName))
    p:int = 10
    print(f'value of p : {p} and object id of p : {id(p)}')
    q:int = p
    print(f'value of q : {q} and object id of q : {id(q)}')
    p:int = 20
    print(f'value of p : {p} and object id of p : {id(p)}')
    print(f'value of q : {q} and object id of q : {id(q)}')
    #Mutable Data Types: list, dict, set, bytearray
    list1: list = [1, 2, 3]
    print(f'list1 : {list1} and object id of list1 : {id(list1)}')
    list2: list = list1
    print(f'list2 : {list2} and object id of list2 : {id(list2)}')
    list1.append(5)
    print(f'list1 : {list1} and object id of list1 : {id(list1)}')
    print(f'list2 : {list2} and object id of list2 : {id(list2)}')
    for i in range(len(userName)):
        print(f'character at index {i} : {userName[i]}')
    dictionary: dict = {"name": "Aniket", "age": 25, "city": "New York"}
    print(f'dictionary : {dictionary} and object id of dictionary : {id(dictionary)}')
    print(f'Name: {dictionary["name"]}, Age: {dictionary["age"]}, City: {dictionary["city"]}')
    print(f'Keys: {list(dictionary.keys())}')
    print(f'Values: {list(dictionary.values())}')
    print(f'Items: {list(dictionary.items())}')
    print(f'Length of dictionary: {len(dictionary)}')
    print(f"object id of dictionary items : {id(dictionary.items())}")
    print(f"object id of dictionary keys : {id(dictionary.keys())}")
    print(f"object id of dictionary values : {id(dictionary.values())}")
    print(f"object id of dict[name] : {id(dictionary['name'])}")
    print(f"object id of dict[age] : {id(dictionary['age'])}")
    print(f"object id of dict[city] : {id(dictionary['city'])}")
    set1: set = {1, 2, 3}
    print(f'set1 : {set1} and object id of set1 : {id(set1)}')
    set2: set = set1
    print(f'set2 : {set2} and object id of set2 : {id(set2)}')
    set1.add(4)
    print(f'set1 : {set1} and object id of set1 : {id(set1)}')
    print(f'set2 : {set2} and object id of set2 : {id(set2)}')
    print(f'Length of set1: {len(set1)}')
if __name__ == "__main__":
        main()
        