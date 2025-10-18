class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        one = 0
        

        while one < len(nums):
            two = one + 1

            while two < len(nums):
                #print(one,two)
                if nums[one] + nums[two] == target:
                    return [one, two]
                two += 1
            one += 1
        #print("all done")
        return [one,two]
