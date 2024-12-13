"""matrix rotation clockwise with using extra matrix. Not an optimal sol, time complexity: O(N^2) and space complexity O(N^2)"""

def mat_rot(matrix):
    n = len(matrix)
    m = len(matrix[0])
    res = [[0 for i in range(n)]  for j in range(m)]
    
    for i in range(n):
        for j in range(m):
            res[j][n-1-i] = matrix[i][j]
    return res


mat = [[1,2,3],
        [4,5,6],
        [7,8,9]]
print(mat_rot(mat))