class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i + len(w)] == w:   # check if its the substring is present in the dictionary
                    dp[i] = dp[i + len(w)]          # if yes, save to cache
                if dp[i]:               # if substring is not present in the dictionary
                    break               # break out and check for the
        return dp[0]
        
        
        
        '''
        # s = "leetcode"
        # store all words in wordict with their first letter, in a hashmap to lookup using a key.
        # move pointer such as: r += len(wordDict[n]) where n is the index of the word found in the wordDict.
        i = j = 0
        while i < len(s) - 1:       # the word to find
            while j < len(wordDict):
                if s[i] == wordDict:   # if a key with the same first letter exists
                    # check if the word is the exact same
                    if visit[s[i]] == s[i:len(visit[s[i]])]:     # slicing "leaves one out"
                        i += len(word) 
                
            # if no key exists in the visit hashmap:
            else:
                return False

        return True 
        '''