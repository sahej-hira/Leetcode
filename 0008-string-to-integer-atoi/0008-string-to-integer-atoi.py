        # ignore space at index[0]
        # if "-" in 0 then the resulatant "int" should be negative
        # return from the first non-zero digit in string, if none: return 0
        # rounding: if num is lesser than -2^31 return -2^31, else if greater than 2^31 - 1 return 2^31 - 1.
class Solution:
    def myAtoi(self, s: str) -> int:
        sign,i = 1,0
        num,result = 0,0

        # Skip leading spaces
        s = s.lstrip(" ")
        if not s: return 0
        print("spaces gone: ",s)

        # watch the sign
        if s[0] == '-':
           sign = -1
           i += 1
        elif s[0] == "+":   # in some testcases there exists "+" sign in others "no sign" implies a positive number
            i += 1
        print("sign noticed: ",sign)

        def traverse(i, num, s):
            #print(i,num)
            # base condition:
            if not s: return 0
            if i >= len(s):
                print("fell")
                return num

            ## recursive condition:
            if s[i].isdigit():
                print("in recursion")
                num = num*10 + int(s[i])
                print("num: ",num)
                return traverse(i + 1, num, s)

            # if not digit
            print("Returning num= ",num)
            return num

        result = traverse(i,num, s) # calling the recursive function
        print("recursive function done: ",result)

        result *= sign  #concatinating the sign
        print("sign and result: ",result)

        # Clamp the result to the 32-bit signed integer range
        int_min, int_max = -2**31, 2**31 - 1
        if result < int_min:
            return int_min
        if result > int_max:
            return int_max
        return result


            