class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        pacificSet = set()
        atlanticSet = set()
        res = []

        def dfs(r, c, ocean, prevHeight):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in ocean or prevHeight > heights[r][c]:
                return

            ocean.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, ocean, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, pacificSet, heights[r][0])
            dfs(r, COLS - 1, atlanticSet, heights[r][COLS - 1])
        for c in range(COLS):
            dfs(0, c, pacificSet, heights[0][c])
            dfs(ROWS - 1, c, atlanticSet, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacificSet and (r, c) in atlanticSet:
                    res.append((r, c))
        
        return res