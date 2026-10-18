class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(i):
            if i < 3:
                return i
            if i in memo:
                return memo[i]
            
            memo[i] = dp(i - 2) + dp(i - 1)
            return memo[i]
        
        return dp(n)