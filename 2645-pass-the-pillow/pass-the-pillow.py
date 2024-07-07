class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        num = time // (n - 1)
        res = time % (n - 1)

        if num%2 == 0:  # from left
            return 1 + res
        #else           # from right 
        return n - res
