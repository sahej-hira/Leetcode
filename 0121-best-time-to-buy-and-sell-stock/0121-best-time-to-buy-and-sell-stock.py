class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        l = 0
        r = 1
        diff = 0 #prices[r] - prices[l] 
        for i in range(1,len(prices) ):
            

            if prices[l] > prices[i - 1]:
               l = i - 1
               r = i 
            elif prices[r] < prices[i]:
                r = i 
            diff = max(prices[r] - prices[l],diff)
            #print("l:",l,"r:",r,"diff:",diff,"prices[r]",prices[r])
        return diff
