class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_seen = set()
        column_seen = set()


        for r in range(9):
            row_seen = set()
            for c in range(9):
                value = board[r][c]
                if value == '.':
                    continue
                
                if value in row_seen:
                    return False
                row_seen.add(value)

        for c in range(9):
            column_seen = set()
            for r in range(9):
                value = board[r][c]
                if value == '.':
                    continue
                if value in column_seen:
                    return False
                column_seen.add(value)
                    
        for box_row in range(3):
            for box_column in range(3):
                box_seen = set()
                for r in range(3):
                    for c in range(3):
                        actual_row = box_row * 3 + r
                        actual_col = box_column * 3 + c
                        small_value = board[actual_row][actual_col]
                        if small_value == '.':
                            continue
                        if small_value in box_seen:
                            return False 
                        box_seen.add(small_value)
        return True 
        

                
                
