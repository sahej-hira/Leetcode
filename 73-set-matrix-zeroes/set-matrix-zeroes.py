class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        first_row_has_zero = False
        first_col_has_zero = False
        
        # check if first row has a zero
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break
        
        # check if first column has a zero
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break
        
        # use first row and column to mark zeros
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # set zeros based on first row and column
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # set zeros for first row and column if needed
        if first_row_has_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        
        if first_col_has_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        '''
        row, column = len(matrix),len(matrix[0]) # COLUMN, ROW
        rowzero = False
        # marking rows and columns to be zero:
        for r in range(row):
            for c in range(column):
                if matrix[r][c] == 0:
                    matrix[0][c] == 0
                    if r > 0:
                        matrix[0][c] == 0
                    else:
                        rowzero = True

        # making zeroes
        for r in range(1,row ):
            for c in range(1,column):
                if matrix[0][c] == 0 or matrix[r][0] ==0:
                    matrix[r][c] = 0

        # all zeroes are calculated except the 1st row and first column

        # first row
        if matrix[0][0] == 0:               # first row
            for r in range(row):
                matrix[0][c] = 0

        # 1st column
        if rowzero == True:
            for c in range(column):
                matrix[r][0] = 0

        return matrix
        '''


                
         