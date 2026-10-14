class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mProfit = 0
        buyPrice = prices[0]
        for p in prices:
            if p > buyPrice:
                mProfit = max(p - buyPrice, mProfit)
            else:
                buyPrice = p
        return mProfit