import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #dfs solution 
        #mark the visited as 0
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])

        def dfs(r,c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
                return
            else:
                grid[r][c] = '0'
                dfs(r, c+1)
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c-1)
        islands = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r,c)
        return islands