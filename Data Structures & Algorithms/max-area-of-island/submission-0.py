class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        maxArea = 0
        visit = set()
        def dfs(r, c):
            area = 1
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r, c) in visit:
                return 0
            
            visit.add((r, c))

            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area

        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(maxArea, dfs(r, c))
        
        return maxArea

            