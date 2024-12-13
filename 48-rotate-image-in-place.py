class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right  = 0, len(matrix) - 1
        while (left < right):
            for i in range(right - left):
                top = left
                bottom = right
                top_left = matrix[top][left + i]
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top+i][right] = top_left
            left += 1
            right -= 1
