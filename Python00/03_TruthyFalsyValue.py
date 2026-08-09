# Assignment01 : Write a Python Program to give an integer value 0 or 1 based on the following: if number is 0 then 0, otherwise 1
class TruthyFalsyValue:
    def __init__ (self, num:float)-> None:
        self.num = num
    def is_truthy(self):
        return int(bool(self.num))
    def power(self, exponent: float,exponent2: float)-> float:
        return self.num ** exponent ** exponent2
    d

if __name__ == "__main__":
    num:float = float(input("Enter a value to check if it's truthy or falsy: "))
    truthy_falsy = TruthyFalsyValue(num)
    print(f"The output for {num} is: {truthy_falsy.is_truthy()}")
    exponent: float = float(input("Enter an exponent to calculate the power: "))
    exponent2: float = float(input("Enter another exponent to calculate the power: "))
    print(f"{num} raised to the power of {exponent} and {exponent2} is: {truthy_falsy.power(exponent, exponent2)}")
    