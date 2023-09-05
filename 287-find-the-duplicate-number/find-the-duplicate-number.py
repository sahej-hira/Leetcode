class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # floyd's fast & slow pointer algorithm

        slow, fast = 0,0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        return slow



        ''' 54/58 test cases aced
        i = 1
        while i < len(nums) - 1:
            if nums[i] in nums[:i]:
                break
            i += 1
        return nums[i]
        '''
        
        
        

        