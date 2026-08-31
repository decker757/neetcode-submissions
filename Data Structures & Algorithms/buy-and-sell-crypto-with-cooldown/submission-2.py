class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[(i, buying)]
            
            cooldown = dp(i + 1, buying)
            if buying:
                buy = dp(i + 1, not buying) - prices[i]
                memo[(i, buying)] = max(buy, cooldown)
            else:
                sell = dp(i + 2, not buying) + prices[i]
                memo[(i, buying)] = max(sell, cooldown)
            
            return memo[(i, buying)]

        return dp(0, True)