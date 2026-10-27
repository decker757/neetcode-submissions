class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        area = 0
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            res = 1

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = 0
                        res += 1
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(bfs(r, c), area)

        return area