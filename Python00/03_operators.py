# import dis
# import struct
# from typing import Any, List


# class ComplexCalculator:
#     """Performs basic arithmetic operations on complex numbers."""

#     def __init__(self, real0: float, imag0: float, real1: float, imag1: float):
#         self.num0 = complex(real0, imag0)
#         self.num1 = complex(real1, imag1)

#     def add(self) -> complex:
#         return self.num0 + self.num1

#     def subtract(self) -> complex:
#         return self.num0 - self.num1

#     def multiply(self) -> complex:
#         return self.num0 * self.num1

#     def divide(self) -> complex:
#         return self.num0 / self.num1

#     def display_operations(self) -> None:
#         print(f"Addition: {self.add()}")
#         print(f"Subtraction: {self.subtract()}")
#         print(f"Multiplication: {self.multiply()}")
#         print(f"Division: {self.divide()}")


# class ListOperationDemo:
#     """Demonstrates list concatenation methods and bytecode differences."""

#     @staticmethod
#     def array_inplace_concatenate() -> List[int]:
#         x = [1, 2]
#         x += [3, 4]
#         return x

#     @staticmethod
#     def array_concatenate() -> List[int]:
#         x = [1, 2]
#         x = x + [3, 4]
#         return x

#     @staticmethod
#     def show_inplace_vs_concatenate() -> None:
#         print(ListOperationDemo.array_inplace_concatenate())
#         print(ListOperationDemo.array_concatenate())

#     @staticmethod
#     def show_bytecode() -> None:
#         def f():
#             x = [1, 2]
#             x += [3, 4]

#         dis.dis(f)

#     @staticmethod
#     def show_mutable_behavior() -> None:
#         a = [1, 2]
#         b = a
#         a += [3, 4]
#         print(a)
#         print(b)

#         a = [1, 2]
#         b = a
#         a = a + [3, 4]
#         print(a)
#         print(b)


# class NumberComparator:
#     """Demonstrates basic number comparisons and boolean operations."""

#     @staticmethod
#     def compare_ints() -> None:
#         a = int(input("Enter a number: "))
#         b = int(input("Enter another number: "))
#         diff = a - b
#         if diff > 0:
#             print(f"{a} is greater than {b}")
#         elif diff < 0:
#             print(f"{a} is less than {b}")
#         else:
#             print(f"{a} is equal to {b}")

#     @staticmethod
#     def compare_floats() -> None:
#         c = float(input("Enter a number: "))
#         d = float(input("Enter another number: "))
#         c_bool = bool(c)
#         d_bool = bool(d)

#         if c > d:
#             print(f"{c} is greater than {d}")
#         elif c < d:
#             print(f"{c} is less than {d}")
#         else:
#             print(f"{c} is equal to {d}")

#         if c_bool ^ d_bool:
#             print(f"Exactly one of {c} or {d} is non-zero")
#         if not (c_bool or d_bool):
#             print(f"Both {c} and {d} are zero")

#         print(f"c_bool: {c_bool}, d_bool: {d_bool}")
#         if c_bool and d_bool:
#             print(f"Both {c} and {d} are non-zero")


# class TruthinessChecker:
#     """Tests truthiness and falsiness of Python data structures."""

#     @staticmethod
#     def check_falsy_values() -> None:
#         values = [
#             None,
#             "",
#             [],
#             (),
#             {},
#             set(),
#             frozenset(),
#             bytearray(),
#             bytes(),
#             range(0),
#             memoryview(b""),
#             complex(0, 0),
#             0.0,
#         ]
#         names = [
#             "None",
#             "Empty string",
#             "Empty list",
#             "Empty tuple",
#             "Empty dict",
#             "Empty set",
#             "Empty frozenset",
#             "Empty bytearray",
#             "Empty bytes",
#             "Empty range",
#             "Empty memoryview",
#             "Zero complex",
#             "Zero float",
#         ]
#         for val, name in zip(values, names):
#             print(f"{name} is falsy: {int(bool(val))}")

#     @staticmethod
#     def check_truthy_values() -> None:
#         truthy_values = [
#             1,
#             -1,
#             0.1,
#             -0.1,
#             "non-empty string",
#             [1],
#             (1,),
#             {1: "a"},
#             {1},
#             frozenset({1}),
#             bytearray(b"1"),
#             bytes(b"1"),
#             range(1),
#             memoryview(b"1"),
#             complex(1, 1),
#         ]
#         for value in truthy_values:
#             print(f"{value} is truthy: {bool(value)}")


# class NumberConverter:
#     """Base interface for all converter implementations."""

#     def convert(self, value: Any) -> Any:
#         raise NotImplementedError


# class FloatToBinaryConverter(NumberConverter):
#     def convert(self, x: float) -> str:
#         if not isinstance(x, (int, float)):
#             raise TypeError("Input must be a number.")
#         packed = struct.pack(">f", float(x))
#         bits = bin(int.from_bytes(packed, byteorder="big"))[2:]
#         return bits.zfill(32)


# class BinaryToFloatConverter(NumberConverter):
#     def convert(self, b: str) -> float:
#         if not isinstance(b, str):
#             raise TypeError("Input must be a string.")
#         int_value = int(b, 2)
#         packed = int_value.to_bytes(4, byteorder="big")
#         return struct.unpack(">f", packed)[0]


# class DecimalToOctalConverter(NumberConverter):
#     def convert(self, n: int) -> str:
#         if not isinstance(n, int):
#             raise TypeError("Input must be an integer.")
#         return f"{n:o}"


# class DecimalToHexConverter(NumberConverter):
#     def convert(self, decimal_number: int) -> str:
#         if not isinstance(decimal_number, int):
#             raise TypeError("Input must be an integer.")
#         return f"{decimal_number:x}"


# class FloatToOctalConverter(NumberConverter):
#     def __init__(self, max_fractional_digits: int = 10):
#         self.max_fractional_digits = max_fractional_digits

#     def convert(self, f: float) -> str:
#         if not isinstance(f, (int, float)):
#             raise TypeError("Input must be a number (int or float).")

#         sign = "-" if f < 0 else ""
#         f = abs(f)
#         integer_part = int(f)
#         fractional_part = f - integer_part

#         octal_integer = f"{integer_part:o}"
#         octal_fractional = []

#         for _ in range(self.max_fractional_digits):
#             if fractional_part == 0:
#                 break
#             fractional_part *= 8
#             digit = int(fractional_part)
#             octal_fractional.append(str(digit))
#             fractional_part -= digit

#         if octal_fractional:
#             return f"{sign}{octal_integer}.{''.join(octal_fractional)}"
#         return f"{sign}{octal_integer}"


# class OctalToFloatConverter(NumberConverter):
#     def convert(self, octal_str: str) -> float:
#         if not isinstance(octal_str, str):
#             raise TypeError("Input must be a string.")

#         octal_str = octal_str.strip()
#         if not octal_str:
#             raise ValueError("Input string cannot be empty.")

#         sign = 1.0
#         if octal_str.startswith("-"):
#             sign = -1.0
#             octal_str = octal_str[1:]
#         elif octal_str.startswith("+"):
#             octal_str = octal_str[1:]

#         if "." in octal_str:
#             integer_part_str, fractional_part_str = octal_str.split(".", 1)
#         else:
#             integer_part_str, fractional_part_str = octal_str, ""

#         integer_part = int(integer_part_str, 8) if integer_part_str else 0
#         fractional_part = 0.0

#         for i, digit in enumerate(fractional_part_str):
#             fractional_part += int(digit, 8) * (8 ** -(i + 1))

#         return sign * (integer_part + fractional_part)


# class HexToDecimalConverter(NumberConverter):
#     def convert(self, hex_str: str) -> int:
#         if not isinstance(hex_str, str):
#             raise TypeError("Input must be a string.")
#         return int(hex_str, 16)


# class ConversionService:
#     def __init__(self):
#         self.converters = {}

#     def register_converter(self, name: str, converter: NumberConverter) -> None:
#         self.converters[name] = converter

#     def convert(self, name: str, value: Any) -> Any:
#         if name not in self.converters:
#             raise ValueError(f"Unknown converter: {name}")
#         return self.converters[name].convert(value)


# class LogicalOperatorDemo:
#     @staticmethod
#     def run() -> None:
#         op1 = input("Enter a boolean value (True/False) for op1: ").strip().lower() == "true"
#         op2 = input("Enter a boolean value (True/False) for op2: ").strip().lower() == "true"

#         if op1 and op2:
#             print(f"Both {op1} and {op2} are True")
#         if op1 or op2:
#             print(f"At least one of {op1} or {op2} is True")
#         if not op1:
#             print(f"{op1} is False")
#         if not op2:
#             print(f"{op2} is False")
#         if op1 ^ op2:
#             print(f"Exactly one of {op1} or {op2} is True")


# class BitwiseOperatorDemo:
#     @staticmethod
#     def run_interactive() -> None:
#         bitwise_a = int(input("Enter an integer for bitwise operations (a): "))
#         bitwise_b = int(input("Enter another integer for bitwise operations (b): "))
#         print(f"Bitwise AND: {bitwise_a & bitwise_b}")
#         print(f"Bitwise OR: {bitwise_a | bitwise_b}")
#         print(f"Bitwise XOR: {bitwise_a ^ bitwise_b}")
#         print(f"Bitwise NOT of a: {~bitwise_a}")
#         print(f"Bitwise NOT of b: {~bitwise_b}")
#         print(f"Left shift of a by 1: {bitwise_a << 1}")
#         print(f"Right shift of a by 1: {bitwise_a >> 1}")
#         print(f"Bitwise XNOR: {~(bitwise_a ^ bitwise_b)}")

#     @staticmethod
#     def run_fixed_example() -> None:
#         x = 13
#         y = 25
#         print(x & y)
#         print(x | y)
#         print(x ^ y)
#         print(~x)
#         print(x << 2)
#         print(x >> 2)
#         print(~(x ^ y))

#     @staticmethod
#     def run_conditional_example() -> None:
#         b = 1
#         c = 1
#         d = 0
#         if 0 and 0 == 0:
#             print("1 Python 3.12.12")
#         if b or b - 1 == 0:
#             print("2 Python 3.12.12")
#         if c or c - 1 == 0:
#             print("3 Python 3.12.12")
#         if d or d + 1 == 0:
#             print("4 Python 3.12.12")


# def main() -> None:
#     ListOperationDemo.show_inplace_vs_concatenate()
#     ListOperationDemo.show_bytecode()
#     ListOperationDemo.show_mutable_behavior()

#     NumberComparator.compare_ints()
#     NumberComparator.compare_floats()

#     TruthinessChecker.check_falsy_values()
#     TruthinessChecker.check_truthy_values()

#     calc = ComplexCalculator(3, 5, 12, 14)
#     calc.display_operations()

#     conversion_service = ConversionService()
#     conversion_service.register_converter("float_to_binary", FloatToBinaryConverter())
#     conversion_service.register_converter("binary_to_float", BinaryToFloatConverter())
#     conversion_service.register_converter("decimal_to_octal", DecimalToOctalConverter())
#     conversion_service.register_converter("float_to_octal", FloatToOctalConverter())
#     conversion_service.register_converter("octal_to_float", OctalToFloatConverter())
#     conversion_service.register_converter("hex_to_decimal", HexToDecimalConverter())
#     conversion_service.register_converter("decimal_to_hex", DecimalToHexConverter())

#     x_float = float(input("Enter a float to convert to binary: "))
#     binary_repr = conversion_service.convert("float_to_binary", x_float)
#     print(f"{x_float} -> {binary_repr}")

#     binary_input = input("Enter a binary string to convert to float: ")
#     float_value = conversion_service.convert("binary_to_float", binary_input)
#     print(f"{binary_input} -> {float_value}")

#     decimal_number = int(input("Enter a decimal to convert to octal: "))
#     octal_number = conversion_service.convert("decimal_to_octal", decimal_number)
#     print(f"{decimal_number} in octal: {octal_number}")

#     decimal_number_hex = int(input("Enter a decimal to convert to hex: "))
#     hex_number = conversion_service.convert("decimal_to_hex", decimal_number_hex)
#     print(f"{decimal_number_hex} in hex: {hex_number}")

#     decimal_float_octal = float(input("Enter a decimal float to convert to octal: "))
#     octal_float = conversion_service.convert("float_to_octal", decimal_float_octal)
#     print(f"{decimal_float_octal} in octal: {octal_float}")

#     octal_input = input("Enter an octal string to convert to decimal float: ")
#     decimal_float_value = conversion_service.convert("octal_to_float", octal_input)
#     print(f"{octal_input} in decimal float: {decimal_float_value}")

#     hex_input = input("Enter a hex string to convert to decimal: ")
#     decimal_value = conversion_service.convert("hex_to_decimal", hex_input)
#     print(f"{hex_input} in decimal: {decimal_value}")

#     LogicalOperatorDemo.run()
#     BitwiseOperatorDemo.run_interactive()
#     BitwiseOperatorDemo.run_fixed_example()
#     BitwiseOperatorDemo.run_conditional_example()


# if __name__ == "__main__":
#     main()

# // CPython Internal Structure (Include/cpython/pytypedobject.h)
# typedef struct {
#     binaryfunc nb_add;
#     binaryfunc nb_subtract;
#     binaryfunc nb_multiply;
#     binaryfunc nb_remainder;
#     binaryfunc nb_divmod;
#     binaryfunc nb_power;
#     binaryfunc nb_negative;
#     ...
#     binaryfunc nb_inplace_add;
#     binaryfunc nb_inplace_subtract;
#     ...
# } PyNumberMethods;
import dis

def add_demo():
    x = [1, 2]
    x = x + [3, 4]  # Creates a brand new PyListObject
    return x
def inplace_demo():
    x = [1, 2]
    x += [3, 4]     # Mutates the existing PyListObject in-place
    return x
print(add_demo())
print(inplace_demo())
#never print
if 0 and 0 == 0:
    print("This will never print!")
# Packed
import struct
packed = struct.pack(">f", 13.37)
print(packed)

class Operators:
    def __init__(self,number1,number2,number3,number4,number5,number6,List1,List2):
        self.number1=number1
        self.number2=number2
        self.number3=number3
        self.number4=number4
        self.number5=number5
        self.number6=number6
        self.List1=List1
        self.List2=List2
        pass
    def concatenateLists(self):
        List2+=self.List1
        return List2
if __name__=="__main__":
    number1:float=float(input("Enter the first number:"))
    number2:float=float(input("Enter the Second number:"))
    number3:float=float(input("Enter the third number:"))
    number4:float=float(input("Enter the first number:"))
    number5:float=float(input("Enter the first number:"))
    number6:float=float(input("Enter the first number:"))
    List1=[1,2,3,4,5]
    List2=[6,7,8,9,10]
    operator=Operators(number1,number2,number3,number4,number5,number6,List1,List2)
    print(operator.concatenateLists())
        
    