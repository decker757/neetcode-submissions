class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def rob_linear(houses: List[int]) -> int:
            memo = {}
            
            def dp(i):
                if i >= len(houses):
                    return 0
                if i in memo:
                    return memo[i]
                
                memo[i] = max(dp(i + 1), dp(i + 2) + houses[i])
                return memo[i]
            
            return dp(0)
        
        res = max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

        return res