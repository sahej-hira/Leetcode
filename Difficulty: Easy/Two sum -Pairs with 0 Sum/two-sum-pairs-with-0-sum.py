#User function Template for python3

class Solution:
    def getPairs(self, arr):
        # code here
        
        
        # Step 2: Initialize a set to store unique pairs and another to track visited elements
        seen = set()
        unique_pairs = set()
        
        # Step 3: Iterate over the array
        for num in arr:
            # Step 4: Check if the opposite of num (-num) exists in the seen set
            if -num in seen:
                # Step 5: Add the pair to the unique_pairs set in sorted order (smallest first)
                unique_pairs.add((min(num, -num), max(num, -num)))
            
            # Step 6: Add the current number to the seen set
            seen.add(num)
        
        # Step 7: Convert the set of pairs to a sorted list and return
        return sorted(list(unique_pairs))
            
        '''
        time limit exceeded:
        # two pointer approach:
        l, r = 0, 0
        n = len(arr) # size of arr
        res = set()
        arr = sorted(arr)
        #[-4,-1,-1,0,1,2]
        
        for l in range(n):
            # 1 - 1 = 0
            # 0 + 1 = 1
            rem = -(arr[l])
            for r in range( l + 1, n):
                if arr[r] == rem and l != r:
                    res.add(tuple((arr[l],arr[r])))
                   
        return sorted(list(res))
        '''
                
            
        
        
        
        
        
        
        '''
        #nt: Instead of implementing a binary search function, consider using a two-pointer approach to find pairs that sum up to zero. This approach can help optimize the code and reduce the time complexity to O(n).
        arr = sorted(arr)
        # [-1,-1,0,1,2,4]
        
        # implement binary search
        ## binary search function to search for remainder
        def bsearch(n,arr):
            l,r = 0,len(arr)
            mid = (l + r)//2
            
            while l < r:
                if arr[mid] == n:
                    return mid
                elif arr[mid] < n:
                    l = mid + 1
                elif arr[mid] > n:
                    r = mid - 1
            
            return 
        
        
        half = len(arr) // 2
        res = []
        for i in range(half):
            rem = 0 - (arr[i])
            ans = bsearch(rem, arr)
            if ans:
                res.append([arr[i], ans])
        return res
        '''
                
            
        
       
            
                    
                    
                    
                    


#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        # matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        obj = Solution()
        res = obj.getPairs(arr)
        if len(res) == 0:
            print()
        else:
            IntMatrix().Print(res)
        print("~")
# } Driver Code Ends