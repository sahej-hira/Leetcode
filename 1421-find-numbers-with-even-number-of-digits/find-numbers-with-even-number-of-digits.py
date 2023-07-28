import math
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evens,count=0,0
        for num in nums:
            


            def int_len(num):#remember local and global variable scope
                #print(num)
                nonlocal count#defining non-local 'count' variable
                count= int(math.log10(num))+1
                #print(count)
                return count

            
            int_len(num)
            #print("here",count)
            if count%2==0:
                evens+=1
        return evens