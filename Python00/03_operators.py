import dis
def arrayInPlaceConcatenate(): 
   x = [1, 2]
   x += [3, 4]   # INPLACE_ADD
   return x
print(arrayInPlaceConcatenate())
def arrayConcatenate():
   x = [1, 2]
   x = x + [3, 4]  # BINARY_ADD
   return x
print(arrayConcatenate())
def f():
    x = [1, 2]
    x += [3, 4]

dis.dis(f)
def g():
    x = 5
    x_id = id(x)
    x += 10                # effectively x = x + 10
    print(x)               # 15
    print(id(x) == x_id)   # False (new object)
g()
def h():
    a = [1, 2]
    b = a           # b refers to the same list
    # +=
    a += [3, 4]     # modifies list in place
    print(a)        # [1, 2, 3, 4]
    print(b)        # [1, 2, 3, 4] (same object)
    # Reset
    a = [1, 2]
    b = a
    # + and =
    a = a + [3, 4]  # creates new list
    print(a)        # [1, 2, 3, 4]
    print(b)        # [1, 2] (old list unchanged)
h()
# def list_sameelementConcatenation():
#    lst += [1]   # modifies default in place!
#    return lst
# print(list_sameelementConcatenation())  # [1]
# print(list_sameelementConcatenation())  # [1, 1]

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

diff = a - b

if diff > 0:
    print(f"{a} is greater than {b}")
elif diff < 0:
    print(f"{a} is less than {b}")
else:
    print(f"{a} is equal to {b}")


c = float(input("Enter a number: "))
d = float(input("Enter another number: "))

# Explicitly convert to bool (like PyObject_IsTrue)
c_bool = bool(c)
d_bool = bool(d)

# But we still need numeric comparison
if c > d:
    print(f"{c} is greater than {d}")
elif c < d:
    print(f"{c} is less than {d}")
else:
    print(f"{c} is equal to {d}")

if c_bool ^ d_bool:  # XOR operation
    print(f"Exactly one of {c} or {d} is non-zero")
if not (c_bool or d_bool):  # NOT operation
    print(f"Both {c} and {d} are zero")
print(f"c_bool: {c_bool}, d_bool: {d_bool}")
if c_bool and d_bool:  # AND operation
    print(f"Both {c} and {d} are non-zero")
# Falsy Values
zeroFromNone=(int)(bool(None))
print(f"None is falsy: {zeroFromNone}")
EmptyString=(int)(bool(''))
print(f"Empty string is falsy: {EmptyString}")
EmptyList=(int)(bool([]))
print(f"Empty list is falsy: {EmptyList}")
EmptyTuple=(int)(bool(()))
print(f"Empty tuple is falsy: {EmptyTuple}")
EmptyDict=(int)(bool({}))
print(f"Empty dict is falsy: {EmptyDict}")
EmptySet=(int)(bool(set()))
print(f"Empty set is falsy: {EmptySet}")
EmptyFrozenSet=(int)(bool(frozenset()))
print(f"Empty frozenset is falsy: {EmptyFrozenSet}")
EmptyByteArray=(int)(bool(bytearray()))
print(f"Empty bytearray is falsy: {EmptyByteArray}")
EmptyBytes=(int)(bool(bytes()))
print(f"Empty bytes is falsy: {EmptyBytes}")
EmptyRange=(int)(bool(range(0)))
print(f"Empty range is falsy: {EmptyRange}")
EmptyMemoryView=(int)(bool(memoryview(b'')))
print(f"Empty memoryview is falsy: {EmptyMemoryView}")
EmptyComplex=(int)(bool(complex(0, 0)))
print(f"Empty complex is falsy: {EmptyComplex}")
EmptyDecimal=(int)(bool(0.0))
print(f"Empty decimal is falsy: {EmptyDecimal}")
# Complex Number Operations
complexNumber0=3+5j
complexNumber1=12+14j
#addition
complexAdd=complexNumber0+complexNumber1
print(f"Addition of {complexNumber0} and {complexNumber1} is: {complexAdd}")
#subtraction
complexSub=complexNumber0-complexNumber1
print(f"Subtraction of {complexNumber0} and {complexNumber1} is: {complexSub}")
#multiplication
complexMul=complexNumber0*complexNumber1
print(f"Multiplication of {complexNumber0} and {complexNumber1} is: {complexMul}")
#division
complexDiv=complexNumber0/complexNumber1
print(f"Division of {complexNumber0} and {complexNumber1} is: {complexDiv}")
# Truthy Values
TruthyValues=[1, -1, 0.1, -0.1, "non-empty string", [1], (1,), {1: 'a'}, {1}, frozenset({1}), bytearray(b'1'), bytes(b'1'), range(1), memoryview(b'1'), complex(1, 1), 0.1]
for value in TruthyValues:
    print(f"{value} is truthy: {bool(value)}")



