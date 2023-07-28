class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i=0
        while i <=len(arr)-1:
            if arr[i]==0:
                arr.insert(i+1,0)
                del arr[len(arr)-1]
                i+=2
            else:
                i+=1







        '''
        for i in range(len(arr)):
            print(arr[i]-1)
            if arr[i]==0:
                
                ind=i+1
                print("0 to be entered",ind)
                for j in range(len(arr)-1,ind-1,-1):
                    if j<len(arr)-1:
                        arr[j+1]=arr[j]
                    else:
                        arr.pop(len(arr)-1)

                #arr[ind]=0    
        '''





















