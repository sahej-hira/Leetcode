from sortedcontainers import SortedSet
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            if abs(i- nums[i]) > 1:
                return False
        return True
       
        '''
       # program for count inversions(gloabal inversions)
        sortedArr = sorted(nums)
        g_inversions = 0    # glocal inversions 
        for i in range(len(nums)):
            if nums[i] > sortedArr[i]:
                g_inversions += (nums[i] - sortedArr[i])
        print("global inversions: ",g_inversions)



       # program for local inversions: (only occurs in neighbours) 
        # l,r = 0, 1
        l_inversions = 0    # local inversions 
        for i in range(1,len(nums)):
            if nums[i - 1]>nums[i]:
                l_inversions += 1
        print("local inversions: ",l_inversions)
            


       # comparison
        if g_inversions == l_inversions:
            return True
        else:
            return False
        '''