class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        prev = groups[0]
        res = [words[0]]
        for i in range(1,len(groups)):        # in the ending point, 1 less elemet i staken in the for loop
            if groups[i] != prev:
                res.append(words[i])
                prev = groups[i]
        return res

