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

    def main(self)->None:
      if not self.name:  
        print(self.happyBirthday()) # the function is called
      else:  
        print(self.happyBirthday(self.name)) # the function with a parameter is called
        
    # def (self,name=None)->None:
    #   print("No name!")
      
if __name__ == "__main__":
    name:str=input("Enter your name: ")
    obj = Functions_and_LambdaFunctions(name)
    obj.main()
    # obj.()