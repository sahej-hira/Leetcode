class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def Sorted(self, s):
        # Code here
        def sort(s):
            if len(s) == 1:
                return 
            temp = s[-1]
            s.pop()
            sort(s)
            insert(s,temp)
            return
        
        def insert(s, temp):
            if not s or s[-1] < temp:
                s.append(temp)
                return
            
            var = s[-1]
            s.pop()
            insert(s,temp)
            s.append(var)
            return 
    
        sort(s)
        return s



#{ 
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.Sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends