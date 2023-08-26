class Solution:
    def reverseWords(self, s: str) -> str:
        # string and list are not mutable in python
        # hence, will have to use some space


        # split s in with " " => will create an array
        # remove all spaces
        # join() with " "

        arr = s.split(" ")  #creating arr
        
        #processing array
        for i in range(len(arr)):
            if '' in arr:
                arr.remove('')

        #string = " ".join(arr[::-1])
        #return string

        return " ".join(arr[::-1]) 
        
        
        ''' not working
        news="" # new string
        for i in range(len(s)):
            if s[i] != " ":
                news += s[i]
            else:
                news += " "
        return news[::-1]
        '''
        
        '''
        ns = s.strip() #new s
        s2 = ""
        for i in range(len(ns)-1,0):
            if ns[i] != " ":
                s2 += ns[i]
            else:
                s2 += " "
        print(s2)
        return s2
        '''

            
