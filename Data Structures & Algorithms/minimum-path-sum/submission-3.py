class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        memo = [[-1] * COLS for _ in range(ROWS)]

        def dp(r, c):
            if r == ROWS - 1 and c == COLS - 1:
                return grid[r][c]
            if r >= ROWS or c >= COLS:
                return float('inf')
            if memo[r][c] != -1:
                return memo[r][c]
            
            memo[r][c] = grid[r][c] + min(dp(r + 1, c), dp(r, c + 1))

            return memo[r][c]
        
        return dp(0, 0)