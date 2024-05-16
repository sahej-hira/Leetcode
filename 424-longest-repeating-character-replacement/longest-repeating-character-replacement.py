class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # using sliding window, hashmap:
        count = {}      # hashmap
        res = 0         # result/ output varible

        l = 0
        for r in range(len(s)):
            # incrementing count of chars in the count hashmap:
            count[s[r]] = 1 + count.get(s[r], 0)

            # condition when we have to move l pointer:
            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            # updating the result:
            res = max(res, r - l + 1)
        return res

            
             