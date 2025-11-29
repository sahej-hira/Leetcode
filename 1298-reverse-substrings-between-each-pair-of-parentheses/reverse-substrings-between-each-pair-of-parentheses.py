class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        rev = []    # array for reversal
        for c in s:
            if c == ")":
                while not st[-1] == "(":
                    rev.append(st.pop())
                st.pop() # remove the "(" from stack
                for i in range(len(rev)): # add to stack after reversing until the whole string isnt reversed
                    st.append(rev[i])
                rev = []

            else:
                st.append(c)
        
        return "".join(st)
                
        