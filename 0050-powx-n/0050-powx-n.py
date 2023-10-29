# by is decreased by a factor of 2

class Solution:
    def myPow(self, x: float, n: int) -> float:
        #print("x:",x,"n:",n)
        if n == 0:
            return 1
        if n == 1:
            return x
        elif n < 0:
            return 1/self.myPow(x,-n)
        else:
            # even power(n):
            if n % 2 == 0:
                return self.myPow( x*x, n//2)

            # odd power(n):
            else:
                return x*self.myPow(x*x, (n - 1)//2)



        