class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        res = 0

        for p in prices[1:]:
            if p > buyPrice:
                profit = p - buyPrice
                res = max(profit, res)
            else:
                buyPrice = p
        
        return res