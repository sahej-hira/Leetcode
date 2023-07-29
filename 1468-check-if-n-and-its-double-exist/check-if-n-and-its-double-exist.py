class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        prevmap={}
        for i,v in enumerate(arr):
            double=v*2
            org=double%2#original
            print(prevmap)
            if v*2 in prevmap or v%2==0 and v/2 in prevmap: #v%2 in prevmap:not right
                print(v,(v*2),v/2)
                return True
            prevmap[v]=i
        return False
            