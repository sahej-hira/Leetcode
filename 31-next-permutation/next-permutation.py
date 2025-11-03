class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        index = -1
        for i in range(len(nums)-2,-1,-1): # start, step, end
            if nums[i] < nums[i + 1]:
                index = i
                break
            
        # no breaking point exists
        if index == -1:
            nums.reverse()
            return nums

        # if the greater value exists:
        for i in range(len(nums)-1,index,-1): # start, step, end
            if nums[index] < nums[i]:
                # swapping 
                nums[index], nums[i] = nums[i],nums[index]
                break
           
        # reversing if there is still some array to the right to get the smallest value
        nums[index + 1:] = reversed(nums[index  + 1:])

        return nums
        