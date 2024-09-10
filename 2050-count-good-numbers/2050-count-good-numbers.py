class Solution:
    def countGoodNumbers(self, n: int) -> int:
        odd = n//2
        even = n//2 + n%2
        MOD = 10**9 + 7

        def power(x,y): # num, no. of occurance
            # base condition:
            if y == 0:      # power = 0
                return 1    # return a**0 = 1
            # recursive condition:
            ans = power(x, y//2) 
            ans *= ans # x**y = x**(y//2)*x**(y//2)
            ans %= MOD
            if y%2 == 1:    # if power is odd :dealing with odd power of x
                ans*= x      # x**3 = (x,1)*(x,1) * (x) = (x^2) * (x) 
            ans %= MOD
            return ans

        return (power(5,even))*(power(4,odd))%MOD








        # correct: but the answer is a vary large value for large testcases.
        # def counting(prod, n, i):
        #     # base condition:
        #     if i >= n:
        #         return prod
        #     if i % 2 == 0:      # even position
        #         val = 5
        #     else:               # odd position
        #         val = 4
        #     # recursive condition:  # to multiply the curretn value with the product
        #     print(val, prod)
        #     print("i: ",i,"n: ",n)
        #     return  counting(prod * val, n, i + 1) # prod * current value of val(4 or 5)
        #     return res%(10^9 + 7)

        # return counting(1, n, 0)
         