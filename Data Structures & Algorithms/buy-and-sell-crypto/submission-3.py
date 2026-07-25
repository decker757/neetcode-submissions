class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy_price = prices[0]
        for p in prices:
            if p > buy_price:
                profit = p - buy_price
                res = max(profit, res)
            else:
                buy_price = p
        return res

