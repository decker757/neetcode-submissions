class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        res = 0
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1: # fresh fruits count them
                    fresh += 1
                elif grid[r][c] == 2: # appending the rotten fruits to the q
                    q.append((r, c))
            
        while q and fresh:
            res += 1
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
            
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                            fresh -= 1
                            grid[nr][nc] = 2
                            q.append((nr, nc))

        return res if fresh == 0 else -1
