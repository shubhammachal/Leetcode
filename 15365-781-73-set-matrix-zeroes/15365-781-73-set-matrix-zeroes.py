class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #instead of extra space for row and col to keep track of 0
        # use first row and first col
        # then based on that 0, fill rest of the matrix based on the cond as 0
        rows = len(matrix)
        cols = len(matrix[0])
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))

        #mark element in first row and col as 0 if we find a 0 in that row or col
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        #based on first row and first col, mark other as zeros
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        #if first row has any zero before or first col had any zero before
        #mark whole row as 0 and col as zero
        if first_row_has_zero:
            for j in range(cols):
                matrix[0][j] = 0
        if first_col_has_zero:
            for i in range(rows):
                matrix[i][0] = 0
            
            
        
