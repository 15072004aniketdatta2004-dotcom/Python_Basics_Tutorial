class List:
    def __init__(self,lst):
        self.lst=lst
    def emptyList(self,lst):
        # for k in list(range(0,len(self.lst),-1)):
        #     print(self.lst[k])
        for k in list(range(0,len(self.lst),-1)):
              print(k,self.lst[k])
        import numpy as np
        emptyList=list[range(0,11,-1)]
        emptyArray=np.array(list[range(0,11,-1)])
        print(emptyList,emptyArray)
        print(type(emptyList),type(emptyArray))
        print(id(emptyList),id(emptyArray))
        for l in range(0,0,1):
            print(l)                  
if __name__=="__main__":
    List2=[item.strip().strip('"') for item in input("Enter the list of integers separated by comma: ").split(",")]
    obj=List(List2)
    obj.emptyList(List2)