class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        #check if first row and col has any zeros
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(c))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(r))

        #if element is 0, first element of that row and col = 0
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        #using frist row and first col set elements to 0
        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_has_zero:
            for j in range(c):
                matrix[0][j] = 0

        if first_col_has_zero:
            for i in range(r):
                matrix[i][0] = 0

        
        

        