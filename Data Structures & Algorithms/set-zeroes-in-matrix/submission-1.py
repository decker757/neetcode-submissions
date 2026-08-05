class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        mark = [[matrix[r][c] for c in range(COLS)] for r in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    for i in range(ROWS):
                        mark[i][c] = 0
                    for j in range(COLS):
                        mark[r][j] = 0

    
        for r in range(ROWS):
            for c in range(COLS):
                matrix[r][c] = mark[r][c]
        