class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        count,width = 1,0
        for ind in range(len(s)):
            i = ord(s[ind]) - ord('a')    # finding index of the letter in widths list
            width += widths[i]
            
            if width > 100 :
                count += 1         # increment total number of lines
                width = widths[i]          # holds the width of each line

            print(ind, s[ind], count, width)
        return [count, width]
                
              
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
         
        
        
        
        # i misunderstood the content of "widths" array:
        # res = [0,0]
        # sum = 0
        # for i in widths:
        #     if sum >= 100:
        #         res[0] += 1         # updating number of lines
        #         sum = 0
        #     sum += i
        # res[1] = sum
        # return res


        