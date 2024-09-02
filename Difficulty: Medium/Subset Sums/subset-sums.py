#User function Template for python3
class Solution:
	def subsetSums(self, arr, n):
		# code 
		ans = [0,]
		arr.sort()
		for i in range(n):
		    x = len(ans)
		    ans.append(arr[i])
		    for y in range(1,x):
		        ans.append(arr[i] + ans[y])
		return ans


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