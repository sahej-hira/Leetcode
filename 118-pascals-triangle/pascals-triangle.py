class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # resultant list
        result = []
        # sub lists for the resultant array
        for i in range(numRows):
            row = [None for _ in range(i + 1)]
            row[0],row[-1] = 1,1
            for j in range(1, len(row) - 1):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]
            result.append(row)
        return result

        
        

        