class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #helper to check if row/col is valid
        def rc_helper(nums):
            a = [x for x in nums if x != '.']
            return len(set(a)) == len(a)
        
        def row_check(board):
            for r in board:
                if not rc_helper(r):
                    return False
            return True
        
        def col_check(board):
            for c in zip(*board):
                if not rc_helper(c):
                    return False
            return True
        
        def box_check(board):
            for i in (0, 3, 6):
                for j in (0, 3, 6):
                    box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                    if not rc_helper(box):
                        return False
            return True
        
        return row_check(board) and col_check(board) and box_check(board)
            