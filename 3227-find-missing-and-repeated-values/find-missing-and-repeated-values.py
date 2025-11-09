class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        sn = n**2 # squared n
        res = [0,0]

        squareset = set()

        for i in range(1,sn + 1):
            squareset.add(i)

        #print(squareset)

        
        for r in range(len(grid)):# nt starting from 0, starting from 1
            for c in range(len(grid[r])):
                if grid[r][c] in squareset: # only the duplicate will be left
                    squareset.remove(grid[r][c])
                else: #if grid[r][c] not in squareset:
                    #squareset.add(grid[r][c])
                    res[0] = grid[r][c]
        #print(squareset)
        res[1] = squareset.pop()
        return res
