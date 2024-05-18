class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = []
        reslen = 0

        for i in range(len(s)):
            l,r = i, i
            while l > -1 and r < len(s) and s[l] == s[r]:
                # whlie the pointers are in bound, updating the lenght of string:
                if (r - l + 1) > reslen:
                    res = s[l: r + 1]
                    reslen = (r - l + 1)

                # updating loop pointers:
                l -= 1
                r += 1

            l,r = i, i + 1
            while l > -1 and r < len(s) and s[l] == s[r]:
                # whlie the pointers are in bound, updating the lenght of string:
                if (r - l + 1) > reslen:
                    res = s[l: r + 1]
                    reslen = (r - l + 1)

                # updating loop pointers:
                l -= 1
                r += 1
        return res













































        # def palindrome(s):
        #     if len(s) <= 1:
        #         return True

            
        #     if s[0] == s[len(s) - 1]:
        #         return palindrome(s[1:len(s) - 1]) 

                
        # l,r = 0,len(s) 
        # pal = s[0]
        # '''
        # for r in range(1,len(s)):
        #     print(l,r)
        #     sub = palindrome(s[l:r])
        #     if sub == True:
        #         pal = s[l:r]
                
        #     else:# False/None
        #         l += 1
        # '''
        # while l <= r:
        #     print(l,r,s[l:r])
        #     sub = palindrome(s[l:r])
        #     if sub == True:
        #         pal = s[l:r]
        #         break
                
        #     else:# False/None
        #         if pass:
        #             l += 1
        #         else:
        #             r -= 1

        #         #l += 1 
        #         #r -= 1


        # return pal
            

         