class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    q.append((r, c))
                    grid[r][c] = "0"
                    while q:
                        for _ in range(len(q)):
                            row, col = q.popleft()
                            for dr, dc in directions:
                                if 0 <= dr + row < ROWS and 0 <= dc + col < COLS and grid[dr + row][dc + col] == "1":
                                    q.append((dr + row, dc + col))
                                    grid[row + dr][col + dc] = "0"
                    res += 1

        return res