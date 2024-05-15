class Solution:
    def tribonacci(self, n: int) -> int:
        #if n == 0: return 0
        known = [0,1,1]

        if n < 3:
            return known[n]
            
        for _ in range(3, n + 1): # the last value is non-inclusive
            known[0], known[1], known[2] = known[1], known[2], sum(known)
        return known[-1]


        
        