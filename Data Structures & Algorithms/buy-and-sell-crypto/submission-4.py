class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy_price = prices[0]

        for p in prices:
            buy_price = min(p, buy_price)
            res = max(res, p - buy_price)
        
        return res
        