class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # apply binary search:
        if not nums:
            return False

        l,r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r)//2

            if nums[mid] == target:
                return True

            # for duplicates:
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
                continue

            # figuring out which side is sorted:
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False





        # dont need to sort the array that adds another O(n) to the time complexity
        # # searching the roatation point
        # # making the array non-rotated
        # # applying binary search
        # if len(nums) - 1 == 1 and target == nums[0]:
        #     return True

        # rd = 0 #rotatedat
        # for i in range(len(nums)-1):
        #     print("i:",i)
        #     if nums[i] > nums[i + 1]:
        #         rd = i + 1
        #         print("rd:",rd)
        #         break

        # #print(nums[rd:], nums[:rd])
        
        # nums =  nums[rd :] + nums[:rd]

        
        # print(nums)

        # #binary search
        # l,r = 0,len(nums) - 1

        # while l < r :
        #     m = (l+r)//2
        #     if target < nums[m]:
        #         r = m - 1
        #     elif target > nums[m]:
        #         l = m + 1
        #     elif target == nums[m]:
        #         return True
        #     else:
        #         return False

        # return False






        
        
        
        
        
        
        
        
        
        # why cant we simply look for the target? we can
        # binary seach is more efficient for searching.

        # for n in nums:
        #     if target in nums:
        #         return True

        # return False
        