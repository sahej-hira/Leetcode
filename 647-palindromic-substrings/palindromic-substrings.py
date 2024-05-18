class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0             # int to return 

        for i in range(len(s)):
            # odd palindrome:
            l = r = i
            while l > -1 and r < len(s) and s[l] == s[r]:
                # updating number of palindromes:
                res+= 1

                # updating loop variables:
                l -= 1
                r += 1

            # even palindromes:
            l, r = i, i + 1
            while l > -1 and r < len(s) and s[l] == s[r]:
                # updating number of palindromes:
                res+= 1

                # updating loop variables:
                l -= 1
                r += 1

        return res
        