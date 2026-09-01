class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def linear_rob(houses):
            memo = {}
            def dp(i):
                if i >= len(houses):
                    return 0
                if i in memo:
                    return memo[i]
                memo[i] = max(dp(i + 1), houses[i] + dp(i + 2))

                return memo[i]
            return dp(0)
        
        return max(linear_rob(nums[:-1]), linear_rob(nums[1:]))