class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr):
            rob1 = rob2 = 0
            for n in arr:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        # if len(nums)%2 == 0:
        #     return helper(nums)
        # else:
        if len(nums) == 1 and nums[0] != 0: return nums[0]
        return max(helper(nums[:-1]), helper(nums[1:]))
        