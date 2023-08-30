class Solution:
    def isHappy(self, n: int) -> bool:

        visited = set()     #hashset
        
        while n not in visited:
            visited.add(n)
            n = self.newnum(n)
            if n == 1:
                return True
        #print("value in visited repeated",n)
        return False        # represents duplicacy
    '''
    def helper(self,n):
        for i in range(len(n)):
            SS = i ** 2     # sum of squares
        return SS
        #return sum[int(d)**2 for d in str(n)]
    '''
        
    def newnum(self, n):        # newnum = sum of squares of each num
        res = 0

        while n :               # while n is not None:
            #print(n)

            digit = n % 10
            #print("n after modulus: ",digit)
            
            digit = digit ** 2
            #print("squared digit", digit)

            res += digit
            #print("res",res)
            #print("ugh",n)
            n = n // 10
            #print("n" , n)
        return res
        





        '''
        ones = int(number % 10)
        tenths = int((number * 10) % 10)
        hundredths = int((number * 100) % 10)
        '''
        