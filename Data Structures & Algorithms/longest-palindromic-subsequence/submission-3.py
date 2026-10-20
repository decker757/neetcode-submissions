import sys
sys.setrecursionlimit(10000)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        reversed_s = s[::-1]
        n = len(s)

        memo = {}

        def dp(l, r):
            if l >= n or r >= n:
                return 0
            if (l, r) in memo:
                return memo[(l, r)]
            
            if s[l] == reversed_s[r]:
                memo[(l, r)] = 1 + dp(l + 1, r + 1)
            else:
                memo[(l, r)] = max(dp(l + 1, r), dp(l, r + 1))

            return memo[(l, r)]
        
        return dp(0, 0)
