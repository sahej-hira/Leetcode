class Solution:
    def reverseVowels(self, s: str) -> str:
        t=[]
        vowels=['a','A','e','E','i','I','o','O','u','U']
        t=list(s)
        #print(t)
        l,r=0,len(t)-1
        while l<r:
            if t[l] in vowels and t[r] in vowels:
                #print(t[l],t[r])
                t[l],t[r]=t[r],t[l]
                l += 1
                r -= 1
            elif t[l] in vowels:
                t[l]
                r -= 1
            else:
                t[r]
                l += 1
        
        return ''.join(t)
          
            
            

