#For Loop
# Consider an algorithm that takes as input a positive integer n. If n is even, the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three and adds one. The algorithm repeats this, until n is one. For example, the sequence for n=3 is as follows:
#  3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# Your task is to simulate the execution of the algorithm for a given value of n.
# Input
# The only input line contains an integer n.
# Output
# Print a line that contains all values of n during the algorithm.
# Constraints

# 1 <= n <= 10^6

# Example
# Input:
# 3

# Output:
# 3 10 5 16 8 4 2 1
class Loops:
    def __init__(self,n:int):
        self.n=n
    def weirdNumber(self,n:int):
        while (n!=1):
            print(n,end=' ')
            if(n%2!=0):
                n=(n*3)+1
            elif(n%2==0): 
                n//=2
            else:
                print("the given number is not positive Integer")
        print(1)
    def missingNumber(self,num:list[float])->float:
        # find max using a for loop
        max_val:float=num[0]
        for i in range(1,len(num)):
            if num[i]>max_val:
                max_val=num[i]
        # compute expected sum (1+2+...+n) using a while loop
        expected_sum:float=0.0
        n:int=1
        while n<=int(max_val):
            expected_sum+=n
            n+=1
        # compute actual sum using a for loop
        actual_sum:float=0.0
        for i in range(len(num)):
            actual_sum+=num[i]
        return expected_sum-actual_sum

    def rangePrinter(self):
        threeA = list(range(2,11,2))
        print(threeA)
        threeB = list(range(3,28,5))
        print(threeB)
        threeC = list(range(25,-5,-5))
        print(threeC)
    def rangeAsAGenerator(self,n:int):
        for i in range(0,n):
            yield i
        # print(list(range(5,10,1)))        
    def inList(self,list1:list[int],n:int):
        Li:list[int] = [10,2,-5,19,50]
        for i in range(len(Li)):
            print(Li[i])
        for j in list1:
            print(j)
    def isYummy(self,List:list[str]):
        for f in List:
            flag=int(input(f"enter 0/1 for {f} (0=not yummy, 1=yummy): "))
            match flag:
                case 0:
                    print(f"the food {f} is not yummy")
                case 1:
                    print(f"the food {f} is yummy")
                case _:
                    print(f"Invalid choice for {f}")
    def InverseofAMatrix(self,matrix:list[list[int]]):
        import numpy as np
        from numpy import linalg as LA
        mat = np.array(matrix)
        print("Original Matrix:")
        print(mat)
        m = LA.inv(mat)
        return m
    def naiveSearch(self,list3:list[int],n:int):
        for i in list3:
            if i==n:
                print(f"Number {n} is found in the list for {i}")
                break
            else:
                print(f"Number {n} is not found in the list for {i}")
                continue
            print("the values are:",i)
    def IndexBasedLoopsandElementBasedLoops(self):
        #Element-based loops
        sum=0
        for element in List3:
            sum+=element
        print(sum)
        #Index-based loops
        sum=0
        for i in range(len(List3)):
            sum+=List3[i]
        print(sum)             

        
            
if __name__=="__main__":
    num:int=int(input("enter a positive integer Number:"))
    obj=Loops(num)
    obj.weirdNumber(num)
    number:list[float]=list(map(float,input("enter a number:").split()))
    print(obj.missingNumber(number))
    n:int=int(input("enter a number:"))
    obj.rangePrinter()
    print(list(obj.rangeAsAGenerator(n)))
    List:list[int]=[]
    List = list(map(int, input("enter the list (space-separated): ").split()))
    obj.inList(List,n)
    List2=[item.strip().strip('"') for item in input("Enter the list of food names separated by comma: ").split(",")]
    obj.isYummy(List2)
    d=int(input("Enter the dimension of the matrix: "))
    matrix:list[list[int]]=[]
    for i in range(d):
        row:list[int]=[]
        for j in range(d):
            row.append(int(input(f"Enter the element at position ({i},{j}): ")))
        matrix.append(row)
    print(obj.InverseofAMatrix(matrix))
    print("\n")
    for i in [1,5,3,10,50,14,0]:
        if(i<10):
            continue
        else:
            print(i,end=" ")
    print("\n")
    for i in [1,5,3,10,50,14,0]:
        print(i,end=" ")
        if(i>10):
            break
    List3=[int(item.strip().strip('"')) for item in input("Enter the list of integers separated by comma: ").split(",")]
    obj.naiveSearch(List3,n)      
    obj.IndexBasedLoopsandElementBasedLoops()


#While Loop
