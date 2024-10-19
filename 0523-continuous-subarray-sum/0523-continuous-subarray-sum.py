class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # 1. keep atleast one el in the "subarr" at all times
        # 2. sum(subarr)%k == 0 implies that the sum of els of subarr are a mutiple of k (given value).


        # edge case: 0 is always a multiple of k.
        reminderIndex = {0:-1,} # hashmap for reminder:index
        total = 0

        for i,n in enumerate(nums):
            total += nums[i]
            reminder = total % k
            if reminder not in reminderIndex:
                reminderIndex[reminder] = i   # storing in hashmap
            elif i - (reminderIndex[reminder]) > 1: # and reminder in reminderIndex and (
                return True
            
        
        return False
      


        '''
        reminderIndex = {0:-1,} # hashmap for reminder:index
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            reminder = total % k
            if reminder in reminderIndex and (i - (reminderIndex[reminder]) > 1):
                return True
                #return nums[reminderIndex[reminder] :i]
            reminderIndex[reminder] = i   # storing in hashmap
        
        return False
        '''


