class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # using hashset
        hashset = set()
        for i in nums:
            if i in hashset:    # second instance
            
                #nums.remove(pointer)    
                # above ~ removes all the future instances of the element from the array       
                hashset.discard(i)
                #print(nums)
            else:  #first instance
                hashset.add(i)
            #print(hashset)   
        #print(hashset)  
        # convert hashset to list and fetch
        nlist = list(hashset)
        return nlist[0]
        
        
        '''
        #uses bit manipulation
        el = 0
        for i in nums:
            el = i ^ el #XOR operation
        return el
        '''
    
    
    
        '''NOT WORKING
        #iterative approach
        nums.sort()
        i = 0
        while i < len(nums)-1:
            if nums[i]!=nums[i+1]:
                print(nums[i+1])
                return nums[i]
            i+=1
                
        return nums[i]
        '''
        
        