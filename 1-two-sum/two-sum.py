from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict()
        
        for index, value in enumerate(nums):
            diff = target - value
            if diff in hashmap:
                break
            else:
                hashmap[value] = index
        
        return hashmap.get(diff), index
        
        
        
        
        '''
        from collections import defaultdict

        # Creating a hashmap using defaultdict
        hashmap = defaultdict(int)

        # Adding key-value pairs to the hashmap
        hashmap["key1"] = 10
        hashmap["key2"] = 20
        hashmap["key3"] = 30

        # Accessing values in the hashmap
        print(hashmap["key2"])  # Output: 20
        '''
        