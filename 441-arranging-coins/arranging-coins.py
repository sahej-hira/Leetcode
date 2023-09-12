class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        rowsno = 0
        #print("not enteres")
        for i in range(1,n + 1):

            #print("enteres")
            # for each iteration increase the "subtracting factor"
            #print(i,n)
            #if i > 0:
            if i <= n :
                #print("entered")
                n = n - i
            else:
                break
                
            rowsno += 1
            
            #print(n,rowsno)
        return rowsno
        