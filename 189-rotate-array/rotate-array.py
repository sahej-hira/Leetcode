class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # select no. of elements to shift
        # use slice
        # add to the beginning

        k = k % len(nums) # $
        
        n = 0
        n = len(nums) - k
        head = nums[n:]
        #print(head)
        nums[n:],nums[:n] = nums[:n],nums[n:]

        
        #nums = nums[n:]+nums[:n]
        #print(nums)

        return nums




''' not working
        # fast and slow pointer approach

        kill = len(nums) 
        itr = 1 #iterator
        while itr <= k: #traversing elements to be prepended
            
            kill -= 1
            itr += 1
            #print("itr: ",itr,"k: ",k)
            #print("kill",kill,nums[kill])
            
        
    
        # slice the array for the elements to be prepended
        #preap = nums[kill:] #prepend elements
        #print(preap)    #all correct till here
    
        

        ### shift all the element to the very end from the end
        #print((nums[kill:])[::-1])  #correct
        #nums = nums.insert(0,(nums[kill:])[::-1]) # not working




## work in progress

        
        n = len(nums) - kill
        for i in range(len(nums) - (n + 1),-1,-1): #problem
            #last = len(nums) 
            print(nums)
            # it never is gonna be zero
            nums[i + n],nums[i] = nums[i],nums[i + n]
        
        fel = nums[0]   # pointer to first element
        j = 0
        while j <= n -1 :
            j += 1
            nums[j - 1] = nums[j]
            #print(j, nums[j])
            
        nums[j-1] = fel
        print(nums)
'''
#############################################################################
'''
        
        #rotating all the other elements
        #print(i, nums[i],nums[i - 1])              
        
        #print("arr",nums)
        if i != 0: 
            nums[i] = nums[i - 1] 
        else:
            nums[i] = last
'''

''' time complexity: O(n*k)
        while k > 0:

              # no fakin neeed to pop 
            
            last = nums[len(nums) - 1] 
            for i in range(len(nums) - 1,0 - 1,-1): 
                
                
                #rotating all the other elements
                #print(i, nums[i],nums[i - 1])              
                
                #print("arr",nums)
                if i != 0: 
                    nums[i] = nums[i - 1] 
                else:
                    nums[i] = last
                    

            #print("final arr", nums)
              
            k -= 1
        return nums
'''