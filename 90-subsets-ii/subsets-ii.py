class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        # use recursion
        def backtrack(i, subset):
            # base condition:
            if i == len(nums):
                ans.append(subset[::])  # append the copy of the subset to the ans/output array
                return

            ### to avoid duplicates:

            ## recursive condition:
            # if the subsets are to contain num[i]  ( to be added for the first time only):
            subset.append(nums[i])           # add num[i]
            backtrack( i + 1, subset)
            subset.pop()

            # if the subset do not contain num[i]:
            # skip all the indices that have the same number i.e num[i] - to avoid duplication
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:       # while the next index is not out of bounds and has the sam evalue
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])        # calling the recursive function
        return ans              # return the output


