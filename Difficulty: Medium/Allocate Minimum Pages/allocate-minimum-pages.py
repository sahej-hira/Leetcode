class Solution:
    def findPages(self, arr, k):
        if k > len(arr):
            return -1  # Optional: more students than books → impossible in some variants
        
        low = max(arr)
        high = sum(arr)
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if self.canAllocate(arr, mid, k):
                ans = mid
                high = mid - 1      # try to minimize
            else:
                low = mid + 1
                
        return ans
    
    def canAllocate(self, books, max_pages, k):
        student_count = 1
        current_pages = 0
        
        for pages in books:
            if pages > max_pages:
                return False
                
            if current_pages + pages <= max_pages:
                current_pages += pages
            else:
                student_count += 1
                current_pages = pages  # start new student with this book
                
                if student_count > k:
                    return False  # early exit optimization
        
        return student_count <= k  # Final check — crucial!
                
            
            
