class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)    # generates a list 
        dp[0] = 0   

        for a in range(1, amount + 1):  # 1: included, amount - 1: one value excluded => loop ends when i reaches the value of amount
            for c in coins:
                if a-c >= 0:
                    dp[a] = min(dp[a],1 + dp[a-c])    # dp [7-4] => dp[3]
        return dp[amount] if dp[amount] != amount + 1 else -1

        