class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo1 = {}
        memo2 = {}

        if n == 1:
            return nums[0]

        def dp(i, arr, memo):
            if i >= len(arr):
                return 0
            
            if i not in memo:
                memo[i] = max(dp(i + 1, arr, memo), dp(i + 2, arr, memo) + arr[i])
            return memo[i]
        
        dp1 = dp(0, nums[: n - 1], memo1) 
        dp2 = dp(0, nums[1:], memo2)

        return max(dp1, dp2)