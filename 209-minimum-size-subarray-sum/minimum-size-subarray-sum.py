class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window technique

        l,total = 0,0
        res = float("inf")
        for r in range(len(nums)):
            total = total + nums[r]
            
            while total >= target:
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1
            
        return 0 if res == float("inf") else res
            



        






        ''' would only work for if subarr len was suppose to be 2
        #sort
        # create 2 pointers from the right 
        # calculate acc. to sum > or < target or = . 

        nums.sort()
        r = len(nums) - 1
        while nums[r] > target:
            r -= 1

        l = r - 1
        for while l >= 0:
            sum = nums[l] + nums[r]
            if sum > target:
                r -= 1
                l -= 1
            elif sum == target:
                break
            else:

        '''

            