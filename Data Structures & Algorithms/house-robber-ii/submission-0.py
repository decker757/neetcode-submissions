class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo1 = [-1] * n
        memo2 = [-1] * n

        if n == 1:
            return nums[0]

        def dp(i, arr, memo):
            if i >= len(arr):
                return 0

            if memo[i] != -1:
                return memo[i]
            
            memo[i] = max(arr[i] + dp(i + 2, arr, memo), dp(i + 1, arr, memo))

            return memo[i]
        
        return max(dp(0, nums[:n - 1], memo1), dp(0, nums[1:], memo2))