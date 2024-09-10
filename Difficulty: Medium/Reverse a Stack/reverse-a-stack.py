#User function Template for python3

from typing import List

class Solution:
    def reverse(self,St): 
        #code here
        def reachBottom(St):  # recursively empties the stack
            # base condition:
            if len(St) == 0:
                return
            
            #recursive consition:
            val = St.pop()
            reachBottom(St)
            fill_at_bottom(St,val)
            return
        
        def fill_at_bottom(St,val):
            # base condition:
            if len(St) == 0:    # at the bottom
                St.append(val)
                return          # to stop recursing further
            
            # recusive condition:
            temp = St.pop() # temporarily removing all the element until the stack is empty
            fill_at_bottom(St,val) # popping until the stack is empty and then appendign the val that is required to be inserted.
            St.append(temp) # putting the temporarily removed elements back in the stack.
            return
        
        reachBottom(St)
        return St


#{ 
 # Driver Code Starts

#Initial Template for Python 3

 
for _ in range(int(input())):
    N = int(input())
    St = list(map(int, input().split()))
    ob = Solution()
    ob.reverse(St)
    print(*St)
# } Driver Code Ends