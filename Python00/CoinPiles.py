# You have two coin piles containing a and b coins. On each move, you can either remove one coin from the left pile and two coins from the right pile, or two coins from the left pile and one coin from the right pile.
# Your task is to efficiently find out if you can empty both the piles.
# Input
# The first input line has an integer t: the number of tests.
# After this, there are t lines, each of which has two integers a and b: the numbers of coins in the piles.
# Output
# For each test, print "YES" if you can empty the piles and "NO" otherwise.
# Constraints

# 1 \le t \le 10^5
# 0 \le a, b \le 10^9

# Example
# Input:
# 3
# 2 1
# 2 2
# 3 3

# Output:
# YES
# NO
# YES
#  We just needed some x number of 1s and some y number of 2s and then some y numbers of 2's and 1s to reach a from (0,0)
#solve:  x+2y=a,2x+y=b st. x,y >=0 as they are number of terms 
# and then first equationn*2-second equation :  3y=2a-b,y=(2a-b)/3
# compute y and then 2x=b-y with conditions b-y>=0 and (b-y)%2==0      


class CoinPiles:
    def __init__(self,a:int,b:int):
        self.a = a
        self.b = b
    def solveCoinPilesForTwoVariables(self,a:int,b:int)-> None:
        if((2*a-b) % 3 == 0):
            y :int  = (2*a-b)//3
            if(y>=0 and (b-y)%2==0):
                x:int = (b-y)//2
                if (x>=0):
                    print("YES")
                    print("the number of ",a, "coin piles is ",x)
                    print("the number of ",b, "coin piles is ",y)
                    return
        print("NO")
        return

def main() -> None:
    """Interactive entry point: prompt for test cases and solve."""
    t: int = int(input("Enter the number of Test Cases: "))
    while t > 0:
        a: int = int(input("Please enter the number of a: "))
        b: int = int(input("Please enter the number of b: "))
        coinPiles = CoinPiles(a, b)
        coinPiles.solveCoinPilesForTwoVariables(a, b)
        t -= 1


if __name__ == "__main__":
    main()
