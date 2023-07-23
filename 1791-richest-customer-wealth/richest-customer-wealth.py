class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        sum = 0
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                sum=sum+accounts[i][j]
            print(sum)
            accounts[i]=sum
            sum=0
            print(accounts)
        return max(accounts)