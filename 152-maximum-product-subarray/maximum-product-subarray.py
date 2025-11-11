# dp- kadane's algorithm
# sum doesnt "flip" values when +ve/-ve are encountered.
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = maxprod = minprod = nums[0]
        
        for n in nums[1:]:
            if n < 0:
                minprod, maxprod = maxprod, minprod

           
            minprod = min(minprod*n, n) 
            maxprod = max(maxprod*n, n)
            # print(minprod, maxprod)
            res = max(maxprod, res)
          

        return res


        
        






































    
    '''
        mul = 1
        maxmul = -10

        for i in range(len(nums)):
            mul *= nums[i]
            maxmul = max(mul, maxmul)
            print("mul: ",mul,"maxmul: ",maxmul)
            if nums[i] == 0:
                mul = 1
        return maxmul
    '''
    '''
        l,r = 0,0
        prod = nums[0]            # product
        mprod = 0
        while r <= len(nums) - 1:
            prod = prod*nums[r]
            if prod <= 0:
                prod = 1
            print(prod)
            mprod = max(mprod,prod)
            r += 1
        return mprod
    '''
'''
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        prod = nums[0]  # Initialize product with the first element
        mprod = nums[0] # Initialize max product with the first element

        for i in range(1, len(nums)):
            # Update the product with the current element
            prod *= nums[i]
            
            # If the product becomes 0 or negative, reset it to 1
            if prod <= 0:
                prod = 1

            # Update the maximum product
            mprod = max(mprod, prod)

        return mprod
'''