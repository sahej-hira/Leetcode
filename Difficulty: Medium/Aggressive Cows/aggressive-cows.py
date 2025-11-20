class Solution:
    def aggressiveCows(self, stalls, k):
        # code here
        stalls.sort()
        l,r = 1, max(stalls)-min(stalls)
        ans = 0
        
        while l <= r:
            mid = (l+r)//2
            
            if self.ispossible(mid,stalls,k) == True:
                l = mid + 1
                ans = mid
            else:
                r = mid - 1
        return ans
        
    def ispossible(self,mid,nums,cows):
        placed = 1   #placing the first cow
        lastpos = nums[0]   #last posititon of the cows already placed
        for i in range(1,len(nums)): # first cow already placed at index 0
            if nums[i] - lastpos>= mid:
                lastpos = nums[i]
                placed += 1
            if placed >= cows:  #if all cows are placed
                return True
                
        return False
                
            
            
        