class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # create a dictionary with nums2
        # adn then traverse nums1 and find greater elements if exist

        # creation of dict:
        cache = {}
        for idx, el in enumerate(nums1):
            cache[el] = idx
        print(cache)
        # now we have: {4:0, 1:1, 2:2}  (element: index)

        res = []        # resultant array (output)
        for i in range(len(nums1)):
            res.append(-1)

        stk = [] # stack
        for num in nums2:
            
            while stk and stk[-1] < num:    # because of 'and' the whole expretion becomes a bool and  for loops 'bool' objects are not iterable
                res[cache[stk[-1]]] = num
                stk.pop()
            if num in nums1:
                stk.append(num)
        return res

 