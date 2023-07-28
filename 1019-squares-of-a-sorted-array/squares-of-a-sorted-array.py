class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        nums[0]=nums[0]**2
        print(nums[0])
        '''
        for i in range(len(nums)):
            nums[i]=nums[i]**2
            '''
            print(nums[i-1],nums[i])
            if(nums[i]<nums[i-1]):
                nums[i-1],nums[i]=nums[i],nums[i-1]
                '''
        nums.sort()
        #print(nums)
        return nums

            
