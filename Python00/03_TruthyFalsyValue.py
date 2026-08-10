# Assignment01 : Write a Python Program to give an integer value 0 or 1 based on the following: if number is 0 then 0, otherwise 1
class TruthyFalsyValue:
    def __init__ (self, num:float)-> None:
        self.num = num
    def is_truthy(self):
        return int(bool(self.num))
    def power(self, exponent: float,exponent2: float)-> float:
        return self.num ** exponent ** exponent2
    

if __name__ == "__main__":
    num:float = float(input("Enter a value to check if it's truthy or falsy: "))
    truthy_falsy = TruthyFalsyValue(num)
    a:int = 4
    b:int = 5
    c:int = 6
    d:bool = True
    e:bool = False
    bool1: bool = (d+d) >= 2 and (not e)
    bool2: bool = (not e) and (6*d == 12/2)
    bool3: bool = (d or (e)) and (a > b)
    bool4: bool = d and (a>b)
    bool5: bool = (not d) or (b!=c)
    bool6: bool =  (d and ( not e )) or (a>b)
    bool7: bool = (a%b==2) and ((not d) or e)
    bool8: bool = (a%b==True) and ((not d) or e)
    print(bool1)
    print(bool2)
    print(bool3)
    print(bool4)
    print(bool5)
    print(bool6)
    print(bool7)
    print(bool8)
    print(f"The output for {num} is: {truthy_falsy.is_truthy()}")
    exponent: float = float(input("Enter an exponent to calculate the power: "))
    exponent2: float = float(input("Enter another exponent to calculate the power: "))
    print(f"{num} raised to the power of {exponent} and {exponent2} is: {truthy_falsy.power(exponent, exponent2)}")
    