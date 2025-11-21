class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # no duplicates in soln -> n + 1 in both recursion steps
        res = []
        candidates.sort()

        def dfs(i , combination, sumofsubarr):
            # base steps:
            if sumofsubarr == target:
                res.append(combination.copy())
                return 
            if i >= len(candidates) or sumofsubarr > target:
                return # move on to next elements since the present ones do not satisfy the condition

            # reusion steps:
            combination.append(candidates[i])
            dfs(i + 1, combination, sumofsubarr + candidates[i]) # no duplicates allowed, move forward
            # backtracking step:
            combination.pop()
            idx = i + 1
            while idx < len(candidates) and candidates[idx - 1] == candidates[idx]:
                idx += 1
            dfs(idx, combination, sumofsubarr)

        dfs(0,[],0)
        return res

        