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
#Bitwise Operations
a:float = float(input("Enter a number for converting the number from decimal to binary:"))
# 60 = 0011 1100
print(f"a = {a} (binary: {bin(int(a))})")
#float to binary conversion
import struct

def float_to_binary(f):
    packed = struct.pack('>f', f)  
    bits = bin(int.from_bytes(packed, byteorder='big'))[2:]
    
    bits = bits.zfill(32)
    return bits

x = float(input("Enter a float number to convert to binary: "))
binary_repr = float_to_binary(x)
print(f"{x} -> {binary_repr}")
#Binary to decimal conversion
def binary_to_float(b):
    int_value = int(b, 2)
    packed = int_value.to_bytes(4, byteorder='big')
    return struct.unpack('>f', packed)[0]

binary_input = input("Enter a binary string to convert to float: ")
float_value = binary_to_float(binary_input)
print(f"{binary_input} -> {float_value}")
#Decimal(Integers) to Octal conversion
decimal_number = int(input("Enter a decimal number to convert to octal: "))
octal_number = oct(decimal_number)
print(f"{decimal_number} in octal is: {octal_number}")
#Decimal(Integers) to Hexadecimal conversion
decimal_number = int(input("Enter a decimal number to convert to hexadecimal: "))
hexadecimal_number = hex(decimal_number)
print(f"{decimal_number} in hexadecimal is: {hexadecimal_number}")
#Decimal(floats) to Octal conversion
decimal_float = float(input("Enter a decimal float number to convert to octal: "))
def float_to_octal(f, max_fractional_digits=10):

    if not isinstance(f, (int, float)):
        raise TypeError("Input must be a number (int or float).")
    
    sign = "-" if f < 0 else ""
    f = abs(f)
    
    integer_part = int(f)
    fractional_part = f - integer_part
    octal_integer = oct(integer_part).replace("0o", "")
    
    octal_fractional = []
    for _ in range(max_fractional_digits):
        fractional_part *= 8
        digit = int(fractional_part)
        octal_fractional.append(str(digit))
        fractional_part -= digit
        if fractional_part == 0:
            break
    
   
    if octal_fractional:
        result = f"{sign}{octal_integer}.{''.join(octal_fractional)}"
    else:
        result = f"{sign}{octal_integer}"
    
    return result


try:
    user_input = input("Enter a decimal float number to convert to octal: ")
    decimal_float = float(user_input)
    
    octal_float = float_to_octal(decimal_float)
    print(f"{decimal_float} in octal is: {octal_float}")
    
except ValueError:
    print("Error: Please enter a valid number.")
except Exception as e:
    print(f"Unexpected error: {e}")

#octal to decimal conversion
def octal_to_float(octal_str):
    if not isinstance(octal_str, str):
        raise TypeError("Input must be a string.")
    
    if '.' in octal_str:
        integer_part_str, fractional_part_str = octal_str.split('.')
    else:
        integer_part_str, fractional_part_str = octal_str, ''
    
    integer_part = int(integer_part_str, 8) if integer_part_str else 0
    
    fractional_part = 0.0
    for i, digit in enumerate(fractional_part_str):
        fractional_part += int(digit) * (8 ** -(i + 1))
    
    return integer_part + fractional_part

octal_input = input("Enter an octal string to convert to decimal float: ")
try:
    decimal_float_value = octal_to_float(octal_input)
    print(f"{octal_input} in decimal float is: {decimal_float_value}")
except ValueError:
    print("Error: Please enter a valid octal string.")
#Binary to octal conversion
def binary_to_octal(binary_str):
    if not isinstance(binary_str, str):
        raise TypeError("Input must be a string.")

    decimal_value = int(binary_str, 2)
    octal_value = oct(decimal_value).replace("0o", "")
    return octal_value
#Hexa decimal to binary conversion
# def hex_to_binary(hex_str):
#     if not isinstance(hex_str, str):
#         raise TypeError("Input must be a string.")
    
#     decimal_value = int(hex_str, 16)
#     binary_value = bin(decimal_value).replace("0b", "")
#     return binary_value
#Hexa decimal to decimal conversion
def hex_to_decimal(hex_str):
    if not isinstance(hex_str, str):
        raise TypeError("Input must be a string.")
    
    decimal_value = int(hex_str, 16)
    return decimal_value

hexadecimal_input = input("Enter a hexadecimal string to convert to decimal: ")
try:
    decimal_value = hex_to_decimal(hexadecimal_input)
    print(f"{hexadecimal_input} in decimal is: {decimal_value}")
except ValueError:
    print("Error: Please enter a valid hexadecimal string.")


def decimal_to_hex(decimal_number):
    if not isinstance(decimal_number, int):
        raise TypeError("Input must be an integer.")
    
    hexadecimal_value = hex(decimal_number).replace("0x", "")
    return hexadecimal_value


decimal_input = int(input("Enter a decimal number to convert to hexadecimal: "))
try:
    hexadecimal_value = decimal_to_hex(decimal_input)
    print(f"{decimal_input} in hexadecimal is: {hexadecimal_value}")
except ValueError:
    print("Error: Please enter a valid decimal number.")


# def float_decimal_to_hexadecimal(float_decimal):
#     if not isinstance(float_decimal, (int, float)):
#         raise TypeError("Input must be a number (int or float).")
    
#     sign = "-" if float_decimal < 0 else ""
#     float_decimal = abs(float_decimal)
    
#     integer_part = int(float_decimal)
#     fractional_part = float_decimal - integer_part
    
#     hexadecimal_integer = hex(integer_part).replace("0x", "")
    
#     hexadecimal_fractional = []
#     while fractional_part and len(hexadecimal_fractional) < 10:
#         fractional_part *= 16
#         digit = int(fractional_part)
#         hexadecimal_fractional.append(hex(digit).replace("0x", ""))
#         fractional_part -= digit
    
#     if hexadecimal_fractional:
#         result = f"{sign}{hexadecimal_integer}.{''.join(hexadecimal_fractional)}"
#     else:
#         result = f"{sign}{hexadecimal_integer}"
    
#     return result

# float_input = float(input("Enter a decimal float number to convert to hexadecimal: "))
# try:
#     hexadecimal_float = float_decimal_to_hexadecimal(float_input)
#     print(f"{float_input} in hexadecimal is: {hexadecimal_float}")
# except ValueError:
#     print("Error: Please enter a valid number.")
# # hexadecimal to float conversion
# def hexadecimal_to_float(hexadecimal_str):
#     if not isinstance(hexadecimal_str, str):
#         raise TypeError("Input must be a string.")
    
#     if '.' in hexadecimal_str:
#         integer_part_str, fractional_part_str = hexadecimal_str.split('.')
#     else:
#         integer_part_str, fractional_part_str = hexadecimal_str, ''
    
#     integer_part = int(integer_part_str, 16) if integer_part_str else 0
    
#     fractional_part = 0.0
#     for i, digit in enumerate(fractional_part_str):
#         fractional_part += int(digit, 16) * (16 ** -(i + 1))
    
#     return integer_part + fractional_part 

# hexadecimal_input = input("Enter a hexadecimal string to convert to decimal float: ")
# try:
#     decimal_float_value = hexadecimal_to_float(hexadecimal_input)
#     print(f"{hexadecimal_input} in decimal float is: {decimal_float_value}")
# except ValueError:
#     print("Error: Please enter a valid hexadecimal string.")

# Logical Operators

