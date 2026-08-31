import sys
import typing
import ctypes
# import nanoleafapi
import os
class Functions_and_LambdaFunctions:
    # A constructor is also a method to create objects which is called in the main function 
    # as Functions_and_LambdaFunctions() for non parameterized constructor and 
    # as Functions_and_LambdaFunctions(arguments) for parameterized constructor
    # in the case of parameterized constructor, the arguments are passed in the time of object creation.
    # and in the case of non parameterized constructor, the arguments are passed in the time of method calling.
    # In short, the constructor is used to initialize the objects.
    # Constructors tell in what manner the objects are created and initialised.
    def __init__(self, name:str)->None:
        self.name = name
    # The function is defined here
    def happyBirthday(self, name:str=None)->str:
        if name:
            return f"Happy Birthday to {name}!"
        return "Happy Birthday to You!"
    def say_hello(self,name:str=None)->None:
       if name:
        print(f"Hello {name}!")
       else: 
        print("Hello")
    def averageOfTwoNumbers(self, num1:float, num2:float)->float:
        # if num1 is None:
        #      print("Enter the Value of num1")
        # if num2 is None:
        #     print("Enter the Value of num2")
        sum=num1+num2
        return (sum/2.0) # Return the value of the function
    # declaration     
    def cube(self,num:float)->float:
        # signature of the function is cube(self,num:float)->float, 
        # where self is the instance of the class, num is the parameter of the function, 
        # and float is the return type of the function.
        # Declaration of the function
        # Definition of the function
      return num**3 # Return the value of the function
    def passFunction(self)->None:
        pass
    def processNumber(self, x:float):
        print(id(x)) # object id = 2370777963824
        x=72.0
        print(id(x)) # object id =2370775005072
        return (x+3) # 75
    def funcA(self,a,b):
        print(id(a),id(b)) #Object id(a,b) = 140724970292696 1339019943216
        print(a,b)
    def mySum(self,x,y):
        sum=x+y
        return sum
    def  funcB(self,a,b,c)->None:
        print(a,b,c)
    def my_food(self,food:list[str])->None:
        print(id(food)) # same object reference as fruits
        for x in food:
            print(x,end=" ")
    x=300
    # def unbound_Local_Error(self)->None:
    #      x=x+1
    def    
    def main(self)->None:
      num0:float= float(input("Enter the number whose cube has to be computed:"))
      print(f"The cube of {num0} is: {self.cube(num0)}",end="\n") # function calling 
      num1:float = float(input("Enter num1 value:"))
      num2:float = float(input("Enter num2 value:"))
      print(f"the return type of pass function is: {self.passFunction.__annotations__['return']}") # None  
      y:float=54.0
      print(id(y)) #object id = 2370777963824
      res=self.processNumber(y) 
      print(id(res)) # object id = 2370777965104
      print(res)
      y1:float=4.0 # object id=1339016783440
      print(id(y1))
      self.funcA(12,y)
      self.funcA(y1,y1)
      self.funcA(id(12),id(y))
      self.funcA(id(y1),id(y1))
      if not self.name:
        self.say_hello() #Once the function is defined , we can call this
        print(self.happyBirthday()) # the function is called
        #self.callmeafunction() # AttributeError: 'Functions_and_LambdaFunctions' object has no attribute 'callmeafunction'
        print(self.averageOfTwoNumbers(num1,num2))
      else:
        self.say_hello(self.name)  
        print(self.happyBirthday(self.name)) # the function with a parameter is called
        print(f"average function({num1},{num2})={self.averageOfTwoNumbers(num1,num2)}")
        print(self.cube(2)+self.cube(3))#35 
        a0:int=10
        b0:int=20
        print(id(a0),id(b0))
        c=self.mySum(a0,b0)
        print(id(a0),id(b0))
        print(c)
        print(sys._getframe().f_locals.keys())
        #print(sys.getprofile())
        print(sys._getframe().f_globals.keys())
        print(sys._getframe().f_code.co_name)
        x0:int = 1
        y0:int = 2
        z0:int = 3
        print(self.funcB(x0,y0,z0))
        fruits:list[str]=[input("Enter a fruit name:") for _ in range(3)]
        print(id(fruits)) # same object reference as food arguement in fruits
        print(self.my_food(fruits))
        # x=300
        # self.unbound_Local_Error() UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
        # print(x)
    # def (self,name=None)->None:
    #   print("No name!")
if __name__ == "__main__":
    name:str=input("Enter your name: ")
    obj = Functions_and_LambdaFunctions(name)
    obj.main()
    # obj.()