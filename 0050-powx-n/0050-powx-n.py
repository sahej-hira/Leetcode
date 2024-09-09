class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x,n):       # a wrapper so we dont pass in a negative power 
            # base conditions:
            if n == 0:
                return 1
            if x == 0:
                return 0
            
            # recursive condition:
            res =  pow(x*x,n//2)
            return x*res if n %2 else res

        # outside of the function
        res = pow(x, abs(n))    # pasing in ONLY positive power (of x)
        return res if n >= 0 else 1/res     # handling the case of negative power
        