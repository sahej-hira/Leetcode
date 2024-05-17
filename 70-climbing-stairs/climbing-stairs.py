class Solution:
    def climbStairs(self, n: int) -> int:
        one = two = 1
        for i in range( n - 1):

            temp = one
            one = one + two
            two = temp
        return one
            




        '''
        #print("n:",n)
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            #print(self.climbStairs(n-1) + self.climbStairs(n-2))
            return self.climbStairs(n-1) + self.climbStairs(n-2)
        '''