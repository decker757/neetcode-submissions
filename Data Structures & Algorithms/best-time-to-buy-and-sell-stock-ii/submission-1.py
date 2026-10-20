class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        res = 0
        for p in prices:
            if p > buyPrice:
                profit = p - buyPrice
                res += profit
            buyPrice = p
        return res