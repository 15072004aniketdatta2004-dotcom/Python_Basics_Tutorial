class IfelifElse:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    def compare_numbers(self):
        if self.number2 > self.number1:
            print(f"{self.number2} is greater than {self.number1}")
        elif self.number2 < self.number1:
            print(f"{self.number2} is less than {self.number1}")
        elif self.number2 == self.number1:
            print(f"{self.number2} is equal to {self.number1}")
        else:
            print("Invalid input. Please provide valid numbers.")
        print("Hello There! This is a simple comparison program.")
    def controlFlow(self):
        x = int(input("Enter a number: "))
        print("You entered:", x)
        if x < 10:
            print("The number is less than 10.")
        elif x <= 99:
            print("The number is between 10 and 99.")
        # """ else:
        #        if x <= 99:
        #           print("The number is between 10 and 99.")
        #        else:
        #           print("The number is 100 or greater.")
        # """
        else:
            print("The number is 100 or greater.")
        print("This is a simple control flow demonstration.")    
    def assignment(self,month:str,day:int):
        output_string:str =''
        if (day<=10):
            output_string+="Early "
        if(day>=20):
            output_string+="Late "
        else:
            output_string+="Mid "
        output_string+=month
        print(output_string)
if __name__ == "__main__":
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    comparison = IfelifElse(number1, number2)
    comparison.compare_numbers()
    comparison.controlFlow()
    month:str= input("Enter a month: ") 
    day:int = int(input("Enter a day: "))
    comparison.assignment(month,day)   