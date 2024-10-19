class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
     #Each result of the division is rounded 
     #to the nearest integer greater than or equal to 
     #that element  

     ## implement binary search
     
     # fixing upper and lower bound (to search for the value in)
     l,r = 1,max(nums)  # represents smallest possible value for mid, the largest possible value for mid variable

     while l <= r:
        mid = (l + r)//2
        if sum(math.ceil(num/mid) for num in nums) > threshold:
            l = mid + 1
        else:
            r = mid - 1
     return l
