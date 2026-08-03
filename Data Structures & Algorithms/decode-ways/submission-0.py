class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dp(n):
            if n == len(s):
                return 1

            if n in memo:
                return memo[n]
            
            res = 0
            if s[n] != "0":
                res += dp(n + 1)
            if n + 1 < len(s) and 10 <= int(s[n:n + 2]) <= 26:
                res += dp(n + 2)
            
            memo[n] = res
            return res
        return dp(0)