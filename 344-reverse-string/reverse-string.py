class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l,r=0,len(s)-1        
        while l<r:
            #c updated to new value
            #c=s[r]
            s[l],s[r]=s[r],s[l]
            #s[r]=c
            #print(s[l],s[r])
            r-=1
            l+=1
            #print(s)
        return s




















