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
class ForLoops:
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
        #List Comprehension
    def primeNumber(self):
        Numbers = list(map(int, input("enter the Numbers to check for Prime Numbers (space-separated): ").split()))
        prime_numbers=[elem for elem in Numbers if all(elem%i!=0 for i in range(2,elem)) and elem>1] # Natural Numbers except one which is divisible by self and one
        print(prime_numbers)
#While Loop
class WhileLoops:
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
        pass

    def conditionalChecks(self):
        i=0
        while i<3:
            i=i+1
            if i==2:
                # skip to the top of the loop
                continue
            print("i is not 2, this is",i)
   
    # ── CSES Hard Problem: Factory Machines ──────────────────────────────
    # https://cses.fi/problemset/task/1620
    #
    # Problem:
    #   A factory has n machines, each with a known production time k_i.
    #   Your task is to find the MINIMUM total time needed to produce
    #   exactly t products. Any machine can run in parallel.
    #
    # Idea  → Binary search on the answer (time).
    #   For a candidate time T, each machine i can produce  T // k_i
    #   products.  If the total across all machines >= t, then T is
    #   feasible; otherwise it is too small.
    #
    # Complexity: O(n · log(t · min(k)))
    #
    # Input example:
    #   machines = [3, 2, 5],  t = 8
    #
    #   Answer = 8   (in 8 seconds: machine1→2, machine2→4, machine3→1 = 7?
    #                  actually 8//3=2, 8//2=4, 8//5=1 → 7.  need 8.
    #                  try 9: 9//3=3, 9//2=4, 9//5=1 → 8 ✓  → answer=9?
    #                  try 10: 10//3=3,10//2=5,10//5=2 →10 ≥8 ✓
    #                  binary search narrows to 8? let's check:
    #                  t=8, machines=[3,2,5] → answer = 8? 8//3+8//2+8//5=2+4+1=7<8
    #                  so answer = 9.)
    #
    # This method uses  while True: ... if ... break  to run the
    # binary-search loop until the search window collapses.
    # ─────────────────────────────────────────────────────────────────────
    def factoryMachines(self, machines: list[int], t: int) -> int:
        """Return the minimum time to produce exactly t products."""
        lo: int = 0
        hi: int = t * min(machines)          # worst case: slowest-possible single machine

        while True:                          # ← infinite loop
            mid: int = (lo + hi) // 2

            # count how many products ALL machines can make in 'mid' seconds
            total: int = 0
            for k in machines:
                total += mid // k
                if total >= t:               # early exit optimisation
                    break

            # narrow the search window
            if total >= t:
                hi = mid                     # mid is feasible → try smaller
            else:
                lo = mid + 1                 # mid is too small → try larger

            if lo >= hi:                     # ← conditional break
                break

        print(f"Minimum time to produce {t} products = {lo}")
        return lo


if __name__=="__main__":

    num:int=int(input("enter a positive integer Number:"))
    obj=ForLoops(num)
    obj.weirdNumber(num)
    obj.primeNumber()
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
    numberz=int(input("Enter a number"))
    whileobj=WhileLoops(numberz)
    whileobj.conditionalChecks()
    whileobj.weirdNumber(numberz)

    # ── CSES Factory Machines demo ──
    print("\n── CSES Factory Machines (while True + if break) ──")
    machines_input = list(map(int, input("Enter machine times (space-separated, e.g. 3 2 5): ").split()))
    products = int(input("Enter number of products to produce: "))
    whileobj.factoryMachines(machines_input, products)

