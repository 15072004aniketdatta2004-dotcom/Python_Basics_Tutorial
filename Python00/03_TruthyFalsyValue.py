# Assignment01 : Write a Python Program to give an integer value 0 or 1 based on the following: if number is 0 then 0, otherwise 1
class TruthyFalsyValue:
    def __init__ (self, num:float)-> None:
        self.num = num
    def is_truthy(self):
        return int(bool(self.num))

if __name__ == "__main__":
    num:float = float(input("Enter a value to check if it's truthy or falsy: "))
    truthy_falsy = TruthyFalsyValue(num)
    print(f"The output for {num} is: {truthy_falsy.is_truthy()}")