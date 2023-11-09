# search optimally
# matrix is sorted
# comp. the target with  the first element of each list
# OR
# choose a random pivot and comp. the target with it.
## how to randomly select a pivot?
  
'''
apply binary search

choose a middle element and compare
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        while i < len(matrix):
            if matrix[i][0] <= target <= matrix[i][-1]:
                if self.bs(matrix[i], 0, len(matrix[i])-1, target):
                    return True 
            i += 1
        return False

    def bs(self, lt, l, r, target):
        while l <= r:
            mid = (l + r) // 2
            if lt[mid] == target:
                return True
            elif lt[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # until there are no more elements in the matrix 
        i = 0
        while i < len(matrix):
            if matrix[i][0] <= target <= matrix[i][-1]:
                # apply binary search on the list:
                if self.bs(matrix[i],0,len(matrix) - 1,target):
                    return True 
                
            
            i += 1

        return False

   
    def bs(self,lt,l,r,target):
        mid = ((l + r)//2
        print("im here",mid,l,r)
        while l <= r:
            # this is not implementing when l == r.
            print("is l less than r")
            if lt[mid] == target:
                return True

            elif lt[mid] < target:
                print("inc. r")
                l = mid + 1

            else:
                r = mid - 1

        return False
'''
                    



        