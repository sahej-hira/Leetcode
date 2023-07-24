class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        prevmap={}
        for i in range(len(nums)):
            if nums[i] in prevmap:
                return True 
            else:
                prevmap[nums[i]]= 1+prevmap.get(nums[i],0)
        return False




#hashmap & use 'in
#sort and match