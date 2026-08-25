import sys
import numpy
class List:
    def __init__(self,lst):
        self.lst=lst
    def emptyList(self,lst):
        # for k in list(range(0,len(self.lst),-1)):
        #     print(self.lst[k])
        print(id([])) #refering to some object id and memory address where there is nothing
        print(sys.getrefcount([]))#1
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
    def IncreasingList(self,arr:list[int],N:int):
        ans=0
        for i in range(1,N):
            if arr[i-1]>arr[i]:
                ans+=(arr[i-1]-arr[i])
                arr[i]=arr[i-1]
        return ans
    def strictly_Increasing_List(self,arr:list[int]):
        n=len(arr)
        # Step 1: Sort using swaps (Bubble Sort)
        for i in range(n):
            for j in range(0,n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        # Step 2: Fix duplicates to ensure strictly increasing
        for i in range(1,n):
            if arr[i]<=arr[i-1]:
                arr[i]=arr[i-1]+1
        return arr
if __name__=="__main__":
    List2=[item.strip().strip('"') for item in input("Enter the list of integers separated by comma: ").split(",")]
    obj=List(List2)
    obj.emptyList(List2)
    N=int(input("Enter the size of the list: "))
    #How to take a list as an user Input
    arr=[int(input(f"Enter the element at index {i}: ")) for i in range(N)]
    print(f"The minimum number of moves required to make the given List:{arr}as an increasing list is={obj.IncreasingList(arr[:],N)}")
    print(f"The strictly_Increasing_List is:{obj.strictly_Increasing_List(arr)}")