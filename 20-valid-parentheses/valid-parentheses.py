class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #stack
        paranthesis = {")":"(","]":"[","}":"{"} #closing bracket as keys and opening bracket as calue
        for i in s:
            if i in paranthesis: # if i is a closing paranthesis
                if not stack or stack[-1] != paranthesis[i]:
                    return False    # strins do NOT match
                stack.pop() # # if stack[-1] == paranthesis[i]
            else: # if i is an opening brachet
                stack.append(i) # strings Do match
        return not stack # return True when stack is empty




        