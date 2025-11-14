class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # binary search? because its the only way to get O(log n)
        if len(nums) == 1:
            return 0 #0 is the index

        l, r= 0,len(nums) - 1
        

        while l < r:
            mid = (l + r)//2

            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
                

        return l