class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minPrice = float('inf')
        maxProfit = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            profit = price - minPrice
            maxProfit = max(profit, maxProfit)
        return maxProfit
