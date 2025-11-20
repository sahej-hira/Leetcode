# dp question
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res= []
        subset = []
        # recursive
        def dfs(i): # in nested function "self" isnt needed as a parameter
            # base condition:
            if i >= len(nums):
                res.append(subset.copy()) # append a copy of subset in res
                return  # returns to the previous step 
            
            # recursive case
            subset.append(nums[i]) # include 
            dfs( i + 1)
            subset.pop() # enclude -> backtracking: remove the last element
            dfs(i + 1)
            # until all the above steps are completed, recursion doesnt end.
            
        dfs(0)
        return res

