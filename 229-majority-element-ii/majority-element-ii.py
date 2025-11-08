class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # moore's voting algorithm for 2 variables:
        char1,char2, count1,count2 = None, None, 0,0

        for num in nums:
            if num == char1:
                count1+= 1
            elif num == char2:
                count2 += 1
            elif count1 == 0:
                char1,count1 = num, 1
            elif count2 == 0:
                char2,count2 = num, 1
            else:
                count1 -=1
                count2 -= 1

        # Step 2: Verify the candidates
        res = []
        for c in [char1, char2]:
            if c is not None and nums.count(c) > len(nums) // 3:
                res.append(c)

        return res

        # there can atleast be 2 elements that cover n//3 of a given array. (always)

            




        