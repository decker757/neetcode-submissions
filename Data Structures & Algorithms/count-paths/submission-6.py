class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]

        def dp(r, c):
            if r > m and c > n:
                return 0
            if r == m - 1 or c == n - 1:
                return 1
            if memo[r][c] != -1:
                return memo[r][c]
            
            memo[r][c] = dp(r + 1, c) + dp(r, c + 1)
            
            return memo[r][c]

        return dp(0, 0)
