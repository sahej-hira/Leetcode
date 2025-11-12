class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        l, r = 0, len(nums) - 1
        
        # If array is not rotated
        if nums[l] < nums[r]:
            return nums[l]
            
        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
                
        return nums[l]




        # # modified binary search for rotated-partially sorted array
        # l, r = 0, len(nums) - 1

        # while l <= r:
        #     mid = (l + r)//2

        #     if nums[l] > nums[mid] < nums[r]:
        #         return nums[mid]

        #     # return True (statment)
        #     if nums[l] <= nums[mid]:
        #         if nums[l] <= nums[mid] < nums[r]:
        #             r = mid - 1
        #         else:
        #             l = mid + 1
        #     else: 
        #         if nums[l] > nums[mid] >= nums[r]:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
 
 
        # return nums[r]
                
                    

        