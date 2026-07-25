class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = prices[0]
        for p in prices:
            buy_price = min(buy_price, p)
            profit =  p - buy_price
            max_profit = max(max_profit, profit)
        return max_profit