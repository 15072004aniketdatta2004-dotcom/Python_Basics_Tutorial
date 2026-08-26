from numpy import array
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
    def Mutability_of_Lists(self,myList:list[int]):
        myList[0]=int(input('Enter the new first element of the list'))
        print(f'The object id of myList is : {hex(id(myList))}')
        myString="Python"
        print(f'The object id of myString is : {hex(id(myString))}')
        print(myString)
        # myString[0:2]='CP' TypeError: 'str' object does not support item assignment
        from io import StringIO
        myStringBuffer=StringIO()
        print(myStringBuffer.write('CPython'))
        print(f'The object id of myStringBuffer is : {hex(id(myStringBuffer))}')
        # myStringBuffer[0:2].write('CP') TypeError: '_io.StringIO' object is not subscriptable
        print(myStringBuffer.getvalue())
        print(myStringBuffer.tell())
        myStringBuffer.seek(0)
        print(myStringBuffer.getvalue())
        print(myStringBuffer.tell())  
        print(f' The object id of the finalList is : {hex(id(myList))}')
        print(f'The value of finalList is {myList}')
        #List is more general sequence object that allows the individual items to be different type
        from typing import Any
        import numpy as np
        car_plate_attribs:list[Any]=['MH', ' 03 ',' B ',' 2025 ']
        car_plate_attrib=np.array(['MH', ' 03 ',' B ',' 2025 '],dtype=np.str_)
        print(car_plate_attribs)
        print(car_plate_attrib)
        from array import array
        
        # --- Creating an array ---
        # Typecode 'i' = signed int, elements must be in a list/iterable
        arr = array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        print("Array:", arr)
        print("Type :", type(arr))

        # --- Basic access ---
        print("\nFirst element :", arr[0])
        print("Last element  :", arr[-1])
        print("Slice [2:6]   :", arr[2:6])

        # --- Modify elements ---
        arr[0] = 99
        print("\nAfter arr[0]=99:", arr)

        # --- Append & Extend ---
        arr.append(10)
        print("After append(10):", arr)

        arr.extend([11, 12, 13])
        print("After extend    :", arr)

        # --- Insert & Remove ---
        arr.insert(1, 50)          # insert 50 at index 1
        print("After insert(1,50):", arr)

        arr.remove(50)             # remove first occurrence of 50
        print("After remove(50)  :", arr)

        # --- Pop ---
        popped = arr.pop()         # remove & return last element
        print(f"Popped {popped}, array:", arr)

        # --- Search ---
        print("\nIndex of 5  :", arr.index(5))
        print("Count of 99 :", arr.count(99))

        # --- Reverse ---
        arr.reverse()
        print("Reversed    :", arr)
        # --- Length ---
        print("Length      :", len(arr))
        # --- Loop through array ---
        print("\nAll elements:")
        for i, val in enumerate(arr):
            print(f"  arr[{i}] = {val}")

        # --- Convert to list and back ---
        lst = arr.tolist()
        print("\nAs list:", lst)

        # --- Common typecodes ---
        # 'b' = signed char, 'i' = signed int, 'f' = float, 'd' = double
        float_arr = array('f', [1.1, 2.2, 3.3])
        print("\nFloat array:", float_arr)

if __name__=="__main__":
    li=["Python 3.16.2","CPython 3.13.1","PythonCompiler 3.9.5"]
    print(li[0],li[1],li[2],sep="\n")
    print(li[1][7:]) # accessing the substring in list
    List2=[item.strip().strip('"') for item in input("Enter the list of integers separated by comma: ").split(",")]
    obj=List(List2)
    obj.emptyList(List2)
    N=int(input("Enter the size of the list: "))
    #How to take a list as an user Input
    arr=[int(input(f"Enter the element at index {i}: ")) for i in range(N)]
    print(f"The minimum number of moves required to make the given List:{arr}as an increasing list is={obj.IncreasingList(arr[:],N)}")
    print(f"The strictly_Increasing_List is:{obj.strictly_Increasing_List(arr)}")
    myList:list[int]=[item.strip().strip('"') for item in input("Enter the list of integers separated by comma: ").split(",")]
    obj.Mutability_of_Lists(myList)        
    print(hex(id(myList)))