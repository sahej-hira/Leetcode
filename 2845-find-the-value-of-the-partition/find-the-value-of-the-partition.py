class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        mid = len(nums)//2
        ret = float("inf")
        for i in range(1, len(nums)):
            ret = min(ret, abs(nums[i]-nums[i-1]))
        return ret