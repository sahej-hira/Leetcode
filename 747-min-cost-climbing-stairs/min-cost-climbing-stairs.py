class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp solution
        cost.append(0)
        for i in range(len(cost) - 3,-1,-1):
            cost[i] = cost[i] + min(cost[i+1], cost[i + 2])
            #print(cost)
        return min(cost[0],cost[1]) # we can either start from 0th position or from the 1st position.



































        '''
        cost.append(0)      # adding the target value

        # starting from 15 in case of [10,15,20,0] so as to have 2 values after the "last index" to make a single or double jump
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])        # choosing min among the element on one jump and double jump
        return min(cost[0],cost[1])
        '''