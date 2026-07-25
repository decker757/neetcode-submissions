class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[i] or board[r][c] == '#':
                return False

            board[r][c] = '#'

            res = None

            for dr, dc in directions:
                res = res or dfs(r + dr, c + dc, i + 1)

            board[r][c] = word[i]
            return res


        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
