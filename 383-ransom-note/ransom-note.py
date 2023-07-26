class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False
        
        for i in ransomNote:
            if i in magazine:
                magazine=magazine.replace(i,'',1)
                #print(i,magazine)
            else:
                #print("im out")
                return False
        return True
                