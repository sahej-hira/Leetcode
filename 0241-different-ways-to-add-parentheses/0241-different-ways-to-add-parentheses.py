class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # change data type of the input:
        arr = []    # array of characters to use as input  for recursion
        num = 0
        for c in expression:
            if c in "-*+":
                arr.append(num)
                num = 0
                arr.append(c)
            else:
                num = num * 10 + int(c)
        else:
            arr.append(num)             # apending the last number

        # recursion
        def calc(left, right):      # calculation
            ans = []                # output array
            # base case:
            if left == right:
                return [arr[left]]

            # recursion:
            for i in range(left + 1, right, 2):
                left_ans = calc(left, i - 1)
                right_ans = calc(i + 1, right)
                if arr[i] == "*":
                    for l in left_ans:
                        for r in right_ans:
                            ans.append(l * r)
                elif arr[i] == "+":
                    for l in left_ans:
                        for r in right_ans:
                            ans.append( l + r)
                elif arr[i] == "-":
                    for l in left_ans:
                        for r in right_ans:
                            ans.append(l - r)
                else:
                    assert(False)
            return ans

        return calc(0, len(arr) - 1)


        