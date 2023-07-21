class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #print("entered")
        last = m+n-1
        while n > 0 and m>0 :
            #print(m,n,last)
            if nums1[m-1]>=nums2[n-1]:
                nums1[last]=nums1[m-1]
                m-=1

            else:
                nums1[last]=nums2[n-1]
                n -=1
            last-=1

        #leftover nums2 elements
        while n>0:
            nums1[last]=nums2[n-1]
            n,last=n-1,last-1
            #print(nums1)
        return nums1




        '''
        for i in range(len(nums2)):
            print("1)",i,nums1)
        
            if(nums1[m+1]==0):
                print("nums1[-1]",nums1[m+1])
                nums1.pop(nums1[m+1])
                print("2)",nums1)
                
                
            if(nums1[i] <= nums2[i]):
                print("nums1[i] <= nums2[i])",nums1[i],nums2[i])
                nums1[i+1]=nums1[i]
                nums1[i]=nums2[i]
                print("3)",nums1)
        return nums1
        '''