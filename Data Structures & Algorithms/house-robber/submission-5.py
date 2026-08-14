class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(n):
            if n >= len(nums):
                return 0

            if n in memo:
                return memo[n]
            
            memo[n] = max(dp(n + 1), nums[n] + dp(n + 2))

            return memo[n]
        
        return dp(0)