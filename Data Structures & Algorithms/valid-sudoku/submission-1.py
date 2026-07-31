class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            charSet = set()
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                if board[r][c] in charSet:
                    return False
                charSet.add(board[r][c])
        
        for c in range(COLS):
            charSet = set()
            for r in range(ROWS):
                if board[r][c] == ".":
                    continue
                if board[r][c] in charSet:
                    return False
                charSet.add(board[r][c])
        
        for br in range(0, ROWS, 3):
            for bc in range(0, COLS, 3):
                charSet = set()
                for r in range(br, br + 3):
                    for c in range(bc, bc + 3):
                        if board[r][c] == ".":
                            continue
                        if board[r][c] in charSet:
                            return False
                        charSet.add(board[r][c])

        return True