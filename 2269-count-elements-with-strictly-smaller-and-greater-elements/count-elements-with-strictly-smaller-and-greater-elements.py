class Solution:
    def countElements(self, nums: List[int]) -> int:
        least, large = min(nums), max(nums)
        to_remove = 0

        for i in nums:
            # count how many els equal the value of least or large:
            if i == least or i == large:
                to_remove += 1

        return len(nums) - to_remove
        