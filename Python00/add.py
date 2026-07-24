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
    msg: str = "Hello World!"
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
    

if __name__ == "__main__":
    main()
    