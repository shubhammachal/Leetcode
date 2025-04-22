class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #can map each grid as 0 to 8 and then check

        rows = [set () for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == '0' or val == '.':
                    continue
                grid_index = (row // 3) * 3 + (col // 3)

                if val in rows[row] or val in cols[col] or val in grids[grid_index]:
                    return False
                rows[row].add(val)
                cols[col].add(val)
                grids[grid_index].add(val)
        return True