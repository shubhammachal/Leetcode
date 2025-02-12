class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        row_set = set()
        col_set = set()
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)
        for i in range(r):
            for j in range(c):
                if i in row_set or j in col_set:
                    matrix[i][j] = 0


        