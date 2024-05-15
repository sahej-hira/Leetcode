class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # a simple method can be pointers:(i overcomplicated this SIMPLE problem)

        ###########################################
        # iterative dp
        # i pointer for s
        # and j pointer for t 

        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return True if i == len(s) else False
        


        