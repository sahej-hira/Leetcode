class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using a hashmap?
        l,r = 0,len(nums) - 1 # 1-indexed
        print(nums[1],nums[len(nums)-1])

        while l < r:
            sum = nums[l] + nums[r]

            if sum > target:
                r -= 1
            elif sum == target:
                break
            else:
                l += 1
            sum = 0
        return l + 1,r + 1
            


        

        '''
        # use while loop
        # too big a contraints :
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                print(nums[i], nums[j])
                sum = nums[i] + nums[j]
                
                if sum == target:
                    return i + 1,j + 1
                j += 1
            i += 1

        return i + 1,j +1
        '''


            



