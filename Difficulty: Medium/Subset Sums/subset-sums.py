#User function Template for python3
class Solution:

	def findsubset(self, i, arr, res, add, n):
	    
	    ###### base condition:
	    if i == n:
	        res.append(add)
	        return 
	        
	    ###### recursive condiiton
	    # to pick:
	    self.findsubset(i + 1, arr, res, add + arr[i], n)
	    
	    # not to pick:
	    self.findsubset(i + 1, arr, res, add, n)



	def subsetSums(self, arr, n):
		# code here
		res = []
		add = 0
		arr.sort()
		self.findsubset(0,arr, res, add, n)
		return res
		
		

	    
	        
	   
	    

		

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x, end=" ")
        print("")

# } Driver Code Ends