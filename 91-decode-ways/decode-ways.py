class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}       # base case: for if the string is an empty string, we'd wanna return 1

        def dfs(i): # from where to start decoding:
            ## base cases:
            if i in dp:         # if already in cache
                return dp[i]
            if s[i] == "0":       # if string is "0" bcuz "0" alone maps to no character.
                return 0 


            ## recursive case:
            res = dfs(i + 1)
            # checking if the next element can be taken along with the previous one:
            # if there are still elements present in the string after the present one AND
            # if the present element was 1 or 2 
            # and the next element is between 0-6
            # because there are ONLY 26 alphabets in englsih alphabets.
            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
                res += dfs(i + 2)
            # add to cache:
            dp[i] = res
            return res 
        return dfs(0) 

        