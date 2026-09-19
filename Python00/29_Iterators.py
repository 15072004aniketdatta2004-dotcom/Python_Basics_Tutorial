class Iterators:
    def __init__(self):
        pass
    def add(self,number_1,number_2,number_3,number_4,number_5):
        return number_1+number_2+number_3+number_4+number_5
    def main(self):
        numbers:list[float]=list(map(float,input("Enter the list of numbers separated by comma:").split(",")))
        print(self.add(*numbers))
if __name__=="__main__":
    obj=Iterators()
    obj.main()