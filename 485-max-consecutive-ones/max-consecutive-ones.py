class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi=0#3maximum
        con=0 #consecutive 
        for i in range(len(nums)):
            if nums[i]==1:
                con+=1
                
            else:
                con=0
            print(con,maxi)
            maxi=con if con>maxi else maxi
        return maxi
            
