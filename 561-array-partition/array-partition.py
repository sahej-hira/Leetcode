class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        #print(nums)

        sum = 0
        for i in range(0,len(nums),2):
            sum = sum + min(nums[i],nums[i+1])
        #print(sum)
        return sum
            