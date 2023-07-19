import re    #importing regex

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)+1-len(needle)):
            if  haystack[i:i+len(needle)]==needle:
                return i
        return -1



        #if needle not a subset of haysack return -1
        #find first occurrence of needle in haysack 
        #haystack and needle consist of only lowercase English characters
        '''
        y = re.search(needle,haystack)
        if(y == []):
            return -1
        else:
            print(y)
            return 0
        '''



        