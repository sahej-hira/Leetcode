class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        cursum = 0

        for n in nums:
            if cursum<0:
                cursum = 0
            cursum += n
            maxsum = max(maxsum,cursum)
        return maxsum

        '''
        # sliding window approach

        l,r = 0,1
        msum = nums[0]
        for r in range(len(nums) - 1):
            if msum + nums[r] < 0:
                l += 1

            if msum + nums[r] < msum:
        '''



            

        