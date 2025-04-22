class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidRows(board):
            for row in range(9):
                seen = set()
                for col in range(9):
                    if board[row][col] == "." or board[row][col] == '0':
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
            return True 
        
        def isValidCols(board):
            for col in range(9):
                seen = set()
                for row in range(9):
                    if board[row][col] == "." or board[row][col] == '0':
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
            return True
        
        def isValidGrid(board):
            for box_row in range(3):
                for box_col in range(3):
                    seen = set()
                    
                    start_row = box_row * 3
                    start_col = box_col * 3
                    
                    
                    for row_offset in range(3):
                        for col_offset in range(3):
                            row = start_row + row_offset
                            col = start_col + col_offset
                            
                            if board[row][col] == '.' or board[row][col] == '0':  
                                continue
                            
                            if board[row][col] in seen:
                                return False
                            seen.add(board[row][col])
            return True  
        
   
        return isValidRows(board) and isValidCols(board) and isValidGrid(board)
