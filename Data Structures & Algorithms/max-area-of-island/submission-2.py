class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            area = 1
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0 
            
            grid[r][c] = 0
            
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area
            
        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(maxArea, dfs(r, c))
        
        return maxArea
                    