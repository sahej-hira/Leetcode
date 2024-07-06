class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        # we don'y have to do any operations 
        # instead we have to see that we have equal number of all the alphabets present in the carcus.
        dic = defaultdict(int)         # dictionary

        # create a hashmap:
        for w in words:
            for char in w:
                dic[char] += 1

        # print(dic)
        for ikey in dic.values():
            if ikey%len(words) != 0: # reminder is not equal to 0:
                return False
        return True

                



        