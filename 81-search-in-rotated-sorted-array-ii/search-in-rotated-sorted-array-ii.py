class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # why cant we simply look for the target?

        for n in nums:
            if target in nums:
                return True

        return False
        