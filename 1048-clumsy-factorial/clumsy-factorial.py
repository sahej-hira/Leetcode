class Solution:
    def clumsy(self, n: int) -> int:
        stk = []        # stack to hold intermediate result to maintaint he proper order of opertions functions (BODMAS)
        operationsToApply = ["*","/","+","-"]
        j = 0           # iterator for operationsToApply array

        stk.append(n)
        n -= 1

        while n > 0:
            op = operationsToApply[j]
            
            if op == "*":
                stk[-1] *= n
            elif op == "/":
                stk[-1] = int(stk[-1]/n)
            elif op == "+":
                stk.append(n)
            elif op == "-":
                stk.append(-n)
            n -= 1
            j = (j + 1) % 4

        return sum(stk)
        '''
        stack = []  # Stack to hold intermediate results
        operations = ["*", "/", "+", "-"]
        j = 0  # Tracks the current operation index

        # Initial operation with first number
        stack.append(n)
        n -= 1

        while n > 0:
            op = operations[j]
            if op == "*":
                stack[-1] *= n
            elif op == "/":
                stack[-1] = int(stack[-1] / n)  # Integer division
            elif op == "+":
                stack.append(n)
            elif op == "-":
                stack.append(-n)
            n -= 1
            j = (j + 1) % 4  # Rotate through the operations

        return sum(stack)
        '''




        '''
        # recursive sol for fac
        def fac(n):
            if n == 1 or n== 0:
                return 1
            elif n < 0:
                return 0
            else:
                return n* fac(n-1)

        print("fac of 1:" ,fac(1))
        print("fac of 2:" ,fac(2))
        print("fac of 3:" ,fac(3))
        print("fac of 4:" ,fac(4))
        '''


        