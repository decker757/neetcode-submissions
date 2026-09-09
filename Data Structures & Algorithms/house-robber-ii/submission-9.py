class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        res = 0
        def linear_rob(houses: List[int]):
            memo = {}
            def dp(i):
                if i >= len(houses):
                    return 0
                if i in memo:
                    return memo[i]
                
                memo[i] = max(dp(i + 2) + houses[i], dp(i + 1))
                return memo[i]
            return dp(0)

        res = max(linear_rob(nums[:len(nums) - 1]), linear_rob(nums[1:]))

        return res