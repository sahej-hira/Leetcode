class Solution:
    def fib(self, n: int) -> int:
        
        cache = {}      #hashmap
        
        def reoccur(n):         # memorization technique
            res = 0
            if n in cache:                      #if present in hashmap 
                return cache[n]
            
            if n < 2:                           # basic fibonacci 
                res = n
            else:
                res = reoccur(n-1) + reoccur(n-2)
            
            #adding value in hashmap
            cache[n] = res
            return res
        return reoccur(n)
            
        
        
'''
iterative approach
F=0
        if(n==0):
            return 0
        if(n==1):
            return 1
        return self.fib(n-1)+self.fib(n-2)
        

'''
        
'''
def fib(self, N):
    """
    :type N: int
    :rtype: int
    """
    cache = {}
    def recur_fib(N):
        if N in cache:
            return cache[N]

        if N < 2:
            result = N
        else:
            result = recur_fib(N-1) + recur_fib(N-2)

        # put result in cache for later reference.
        cache[N] = result
        return result

    return recur_fib(N)
'''
