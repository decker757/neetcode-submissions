class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = float('-inf')
        buyPrice = prices[0]
        profit = 0

        for p in prices:
            if p > buyPrice:
                profit += p - buyPrice
            buyPrice = p
            res = max(profit, res)
            
        return res