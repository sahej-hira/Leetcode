class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algo resets cursum to 0 everytime the value gets negative. 
        # but it only works when the array consists of positive integers and 0
        # unlike now, when the array contains all integers.
        if len(nums) == 1:
            return nums[0]

        maxsum = (-inf)
        cursum = 0
        subarr = []
        for i in range(len(nums)):
            cursum += nums[i]
            
            maxsum = max(maxsum, cursum)
            cursum = max(cursum, 0)
        return maxsum
