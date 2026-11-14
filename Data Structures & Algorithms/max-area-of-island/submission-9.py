class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            area = 0

            while q:
                row, col = q.popleft()
                area += 1

                for dr, dc in directions:
                    nr, nc = dr + row, dc + col

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        q.append((nr, nc))
            return area
        
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, bfs(r, c))
        
        return res