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
        
if __name__=="__main__":
    num:int=int(input("enter a positive integer Number:"))
    obj=Loops(num)
    obj.weirdNumber(num)
    number:list[float]=list(map(float,input("enter a number:").split()))
    print(obj.missingNumber(number))