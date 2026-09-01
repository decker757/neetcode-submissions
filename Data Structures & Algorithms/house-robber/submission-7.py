class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(n):
            if n >= len(nums):
                return 0
            if n in memo:
                return memo[n]
            memo[n] = max(nums[n] + dp(n + 2), dp(n + 1))
            return memo[n]
        
        return dp(0)
            