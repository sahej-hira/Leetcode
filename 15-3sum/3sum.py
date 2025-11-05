class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() #sorting correctly
        
        for i,a in enumerate(nums):
            #duplicate avoidant logic:
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l,r = i + 1, len(nums) - 1 # mistake to put it outside of the loop

            while l < r:
                sum = a + nums[l] + nums[r]
                #print(sum,a,l,r)
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]]) 

                    # stuck in infinite loop if following lines are not added
                    l += 1
                    while  nums[l] == nums[l-1] and l < r:
                        l += 1
       
        return res
