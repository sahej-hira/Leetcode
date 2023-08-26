class Solution:
    def reverseWords(self, s: str) -> str:
        # create an array
        # iterate thru each element(word)
        # return

    
        words = s.split(" ")
        res = ""

        for index,word in enumerate(words):
            #for letter in word:
            nword = word[::-1]  # new word
            words[index] = nword
        
        res = " ".join(words)
            
        return res
'''        
        ns = s.strip() #new s
        s2 = ""
        for i in range(len(ns)-1,-1,-1):
            
            s2 += ns[i]
            
        print(s2)
        return s2[::-1]
'''           
'''
        ns = "" # new string
        for i in s[::-1]:
            print(i)
            ns += i
        print (ns)
        return ns
'''

