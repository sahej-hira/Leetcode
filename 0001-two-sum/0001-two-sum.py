class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using hashmap
        cache = {} #val:index

        for i,n in enumerate(nums):
            diff = target-nums[i]
            if diff in cache:
                return [cache[diff],i]
            cache[n] = i

        return [] #not needed
 
                
                
                
        
             
        
        
        
        
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        # brute force
        # one = 0
        

        # while one < len(nums):
        #     two = one + 1

        #     while two < len(nums):
        #         #print(one,two)
        #         if nums[one] + nums[two] == target:
        #             return [one, two]
        #         two += 1
        #     one += 1
        # #print("all done")
        # return [one,two]
