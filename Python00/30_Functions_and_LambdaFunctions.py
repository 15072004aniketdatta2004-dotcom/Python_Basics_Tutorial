import sys
import typing
import ctypes
# import nanoleafapi
import os
import numpy as np
import math
import cmath
from decimal import Decimal, getcontext, ROUND_HALF_UP, ROUND_DOWN, ROUND_CEILING
from fractions import Fraction
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
    # def unbound_Local_Error(self)->None:
    #      x=x+1
    x=300
    def sumOfArrays(self)->None:
        # global arr1, arr2, result
        arr1=[float(input(f"Enter the [{i}][{j}] element of array 1: ")) for i in range(0,5) for j in range(0,5)]
        arr2=[float(input(f"Enter the [{i}][{j}] element of array 2: ")) for i in range(0,5) for j in range(0,5)]
        result=np.array(arr1)+np.array(arr2)
        print(result)
    def  myfunc(self)-> float:
        global x
        # x=self.x+1
        x=5
        x=5.0
        print(x)
        return x
    def inPlaceListModifierBySumOfPrevElement(self,LIST:list[float]):
        print(LIST)
        for i in range(1,len(LIST)):
            LIST[i]+=LIST[i-1]
            print(LIST)
    @staticmethod
    def pass_by_Value():
        d="Hello"
        def func(p):
            print(id(p))
            p=p+" ,World"
            print(id(p))
        print(id(d))
        func(d)
        print(d) # Hello
        print(id(d))
    @staticmethod
    def pass_by_reference(list1):
        print(id(list1))
        list1.append(5)
        print(id(list1))
        list1=[1,2,3,4,5]
        print(id(list1))
        def fun(p,q):
            p.append(q)
            print(id(p))
        fun(list1,7)
        print(id(list1))
        print(list1)
    def positionalBinding(self,y,x=1,z=2):
        print("x=",x) 
        print("y=",y) 
        print("z=",z) 
    def append_to(self,element,to=[]):
        to.append(element)
        print(to)
        return to
    def concatenate_strings(self,new_string,string='Hey'):
        string+=new_string
        return string
    def List_appender(self,element,Li=None):
        if Li is None:
            Li=[]
        Li.append(element)
        return Li        
    def decimal_fraction_complex_operations(self)->None:
        """Demonstrates Decimal, Fraction, integer/fractional parts, and complex number operations."""
        print("\n" + "="*60)
        print("  DECIMAL, FRACTION & COMPLEX NUMBER OPERATIONS")
        print("="*60)

        # ── 1. Decimal: Precise decimal arithmetic ──
        print("\n── 1. Decimal Module ──")
        # Floating point pitfall
        print(f"  float:   0.1 + 0.2 = {0.1 + 0.2}")          # 0.30000000000000004
        print(f"  Decimal: 0.1 + 0.2 = {Decimal('0.1') + Decimal('0.2')}")  # 0.3

        # Setting precision
        getcontext().prec = 10
        a = Decimal('1') / Decimal('7')
        print(f"  1/7 with precision 10: {a}")  # 0.1428571429

        getcontext().prec = 50
        pi_approx = Decimal('3.14159265358979323846264338327950288419716939937510')
        print(f"  Pi (50 digits): {pi_approx}")

        # Arithmetic with Decimal
        getcontext().prec = 28  # reset to default
        d1 = Decimal('10.5')
        d2 = Decimal('3.2')
        print(f"  {d1} + {d2} = {d1 + d2}")
        print(f"  {d1} - {d2} = {d1 - d2}")
        print(f"  {d1} * {d2} = {d1 * d2}")
        print(f"  {d1} / {d2} = {d1 / d2}")
        print(f"  {d1} // {d2} = {d1 // d2}")   # floor division
        print(f"  {d1} % {d2}  = {d1 % d2}")    # modulo
        print(f"  {d1} ** 2   = {d1 ** 2}")      # exponentiation

        # Rounding modes
        val = Decimal('2.675')
        print(f"  round(2.675, 2) float:          {round(2.675, 2)}")  # 2.67 (float surprise)
        print(f"  Decimal ROUND_HALF_UP:          {val.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}")
        print(f"  Decimal ROUND_DOWN:             {val.quantize(Decimal('0.01'), rounding=ROUND_DOWN)}")
        print(f"  Decimal ROUND_CEILING:          {val.quantize(Decimal('0.01'), rounding=ROUND_CEILING)}")

        # Useful Decimal methods
        d3 = Decimal('-3.14')
        print(f"  Decimal('-3.14').copy_abs()   = {d3.copy_abs()}")
        print(f"  Decimal('-3.14').copy_negate()= {d3.copy_negate()}")
        print(f"  Decimal('-3.14').as_tuple()   = {d3.as_tuple()}")
        print(f"  Decimal('10.5').sqrt()        = {d1.sqrt()}")
        print(f"  Decimal('10.5').ln()          = {d1.ln()}")
        print(f"  Decimal('10.5').log10()       = {d1.log10()}")

        # ── 2. Fractions: Exact rational arithmetic ──
        print("\n── 2. Fractions Module ──")
        # Creating fractions
        f1 = Fraction(3, 4)         # 3/4
        f2 = Fraction(1, 3)         # 1/3
        f3 = Fraction('0.125')      # from string
        f4 = Fraction(0.5)          # from float  (auto-simplified)
        f5 = Fraction(Decimal('0.3'))  # from Decimal
        print(f"  Fraction(3, 4)          = {f1}")
        print(f"  Fraction(1, 3)          = {f2}")
        print(f"  Fraction('0.125')       = {f3}")
        print(f"  Fraction(0.5)           = {f4}")
        print(f"  Fraction(Decimal('0.3'))= {f5}")

        # Arithmetic with fractions
        print(f"  {f1} + {f2} = {f1 + f2}")     # 13/12
        print(f"  {f1} - {f2} = {f1 - f2}")     # 5/12
        print(f"  {f1} * {f2} = {f1 * f2}")     # 1/4
        print(f"  {f1} / {f2} = {f1 / f2}")     # 9/4
        print(f"  {f1} ** 2   = {f1 ** 2}")     # 9/16

        # Accessing parts
        print(f"  Fraction(3,4).numerator   = {f1.numerator}")
        print(f"  Fraction(3,4).denominator = {f1.denominator}")

        # Limit denominator (approximate irrational as fraction)
        pi_frac = Fraction(math.pi)
        print(f"  Fraction(pi)                 = {pi_frac}")
        print(f"  Fraction(pi).limit_denominator(100) = {pi_frac.limit_denominator(100)}")
        print(f"  Fraction(pi).limit_denominator(10)  = {pi_frac.limit_denominator(10)}")

        # Converting fraction ↔ float ↔ Decimal
        print(f"  float(Fraction(1,3))  = {float(f2)}")
        print(f"  Fraction → Decimal    = {Decimal(f1.numerator) / Decimal(f1.denominator)}")

        # ── 3. Integer & Fractional Parts of a Decimal ──
        print("\n── 3. Integer & Fractional Parts ──")
        num = float(input("  Enter a decimal number (e.g. -7.625): "))

        # math.trunc — truncates toward zero
        print(f"  math.trunc({num})  = {math.trunc(num)}")
        # math.floor — largest integer ≤ num
        print(f"  math.floor({num})  = {math.floor(num)}")
        # math.ceil  — smallest integer ≥ num
        print(f"  math.ceil({num})   = {math.ceil(num)}")
        # int() — same as trunc
        print(f"  int({num})         = {int(num)}")

        # math.modf — splits into (fractional, integer) as floats
        frac_part, int_part = math.modf(num)
        print(f"  math.modf({num})   = fractional: {frac_part}, integer: {int_part}")

        # divmod — (quotient, remainder) when dividing by 1
        q, r = divmod(num, 1)
        print(f"  divmod({num}, 1)   = quotient(int part): {q}, remainder(frac part): {r}")

        # Using Fraction to get exact fractional representation
        exact_frac = Fraction(num).limit_denominator(10000)
        print(f"  Exact fraction of {num} ≈ {exact_frac}")

        # ── 4. Complex Numbers ──
        print("\n── 4. Complex Numbers ──")
        # Creating complex numbers
        c1 = complex(3, 4)       # 3 + 4j
        c2 = 2 - 5j             # literal syntax
        c3 = complex('1+2j')    # from string (no spaces allowed)
        print(f"  c1 = {c1}")
        print(f"  c2 = {c2}")
        print(f"  c3 = {c3}")

        # Accessing parts
        print(f"  c1.real = {c1.real},  c1.imag = {c1.imag}")

        # Arithmetic
        print(f"  c1 + c2 = {c1 + c2}")
        print(f"  c1 - c2 = {c1 - c2}")
        print(f"  c1 * c2 = {c1 * c2}")
        print(f"  c1 / c2 = {c1 / c2}")
        print(f"  c1 ** 2 = {c1 ** 2}")

        # Built-in: abs() gives magnitude |c| = sqrt(a² + b²)
        print(f"  abs(c1)  = |3+4j| = {abs(c1)}")

        # Conjugate: a + bj → a - bj
        print(f"  c1.conjugate() = {c1.conjugate()}")

        # cmath module — math functions for complex numbers
        print(f"  cmath.phase(c1)   = {cmath.phase(c1):.4f} radians")
        print(f"  cmath.phase(c1)   = {math.degrees(cmath.phase(c1)):.2f}°")
        print(f"  cmath.polar(c1)   = (r={cmath.polar(c1)[0]:.4f}, θ={cmath.polar(c1)[1]:.4f})")
        print(f"  cmath.rect(5, 0.9273) = {cmath.rect(5, 0.9273)}  (back to rectangular)")

        # cmath functions
        print(f"  cmath.sqrt(-1)    = {cmath.sqrt(-1)}")
        print(f"  cmath.sqrt(c1)    = {cmath.sqrt(c1)}")
        print(f"  cmath.exp(c1)     = {cmath.exp(c1)}")
        print(f"  cmath.log(c1)     = {cmath.log(c1)}")
        print(f"  cmath.log10(c1)   = {cmath.log10(c1)}")
        print(f"  cmath.sin(c1)     = {cmath.sin(c1)}")
        print(f"  cmath.cos(c1)     = {cmath.cos(c1)}")

        # Euler's identity: e^(iπ) + 1 ≈ 0
        euler = cmath.exp(complex(0, cmath.pi)) + 1
        print(f"  Euler's identity: e^(iπ) + 1 = {euler}  (≈ 0)")
        print(f"  cmath.isclose(euler, 0, abs_tol=1e-15) = {cmath.isclose(euler, 0, abs_tol=1e-15)}")

        print("\n" + "="*60 + "\n")
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
        self.myfunc()
        print(self.myfunc.__func__.__globals__.keys())
        # self.sumOfArrays()
        LIST:list[float]=[float(input(f"Enter the {i+1}th element of list: ")) for i in range(0,5)]
        print(id(LIST))
        print(id(LIST))
        self.pass_by_Value()
        self.pass_by_reference(LIST)
        # list1=list1+[6]
        # print(id(list1))
    # def (self,name=None)->None:
    #   print("No name!")
        self.positionalBinding(3)
        self.positionalBinding(3,5)
        self.positionalBinding(3,5,10)
        choice=input("Choose 'c' for characters , i for integers and f for floats")
        match choice:
            case 'c':
                element=input("Enter the element: ")
                print(self.append_to(element))
            case 'i':
                element=int(input("Enter the element: "))
                print(self.append_to(element))
            case 'f':
                element=float(input("Enter the element: "))
                print(self.append_to(element))
            case _:
                print("Invalid choice")
                print(self.append_to(None))
        match choice:
            case 'c':
                element=input("Enter the element: ")
                print(self.append_to(element))
            case 'i':
                element=int(input("Enter the element: "))
                print(self.append_to(element))
            case 'f':
                element=float(input("Enter the element: "))
                print(self.append_to(element))
            case _:
                print("Invalid choice")
                print(self.append_to(None))
        print(self.concatenate_strings(' Aniket'))
        print(self.concatenate_strings('Hello',' Aniket'))
        Size:int=int(input("Enter the size of the list: "))
        Li:list[any]=[]
        for _ in range(Size):
            element:int=int(input("Enter the element: "))
            Li = self.List_appender(element,Li)
        print(Li)
        self.decimal_fraction_complex_operations()
       
        

if __name__ == "__main__":
    name:str=input("Enter your name: ")
    obj = Functions_and_LambdaFunctions(name)
    obj.main()
    # obj.()
    # global keyword
    x=300
    def global_variable_function():
      global x
      x=x+1
      print(x)
    global_variable_function()
    print(x) # x=301
    def increment_x(x)->float:
        # global x
        return x+1
    print(increment_x(x)) # 302
    print(x) # x=301 
    x2:int=100
    def localUnBoundErrorPrinter():
        # print(x2) #UnboundLocalError: 
        # cannot access local variable 'x2' where it is not associated with a value
        global x2
        x2=5
        print(x2)
    localUnBoundErrorPrinter()
    x3:int=1
    def printer(x3:int)->None:
        print(x3)
        x3:float=float(input("Enter a number: "))
        print(x3)
    printer(x3)
    #Call Stack is require to evaluate this functions below
    # Higher Order Functions
    def hofun(fun,seq):
        return [fun(seq,s) for s in seq]
    def f(seq,i):
        return seq[0]+i
    result = hofun(f,[1,3,2]) # Higher Order Functions
    print(result)
     