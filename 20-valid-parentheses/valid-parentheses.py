class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        hash={")":"(","]":"[","}":"{"}
        stk=[]
         
        for i in s:
            if i in hash:
                if stk and stk[-1]==hash[i]:
                    #print("popped")
                    stk.pop()
                else:
                    return False
            else:
                #print("append")
                stk.append(i)
        if stk == []:
            return True
        #print(stk)
        return False 