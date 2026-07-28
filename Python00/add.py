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
if __name__ == "__main__":
    main()
    