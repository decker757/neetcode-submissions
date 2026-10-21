class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(amt):
            if amt <= 0:
                return 0
            if amt in memo:
                return memo[amt]

            res = amount + 1
            for c in coins:
                if amt - c >= 0:
                    res = min(1 + dp(amt - c), res)
                memo[amt] = res
            
            return memo[amt]
        
        minCoins = dp(amount)

        return -1 if minCoins >= amount + 1 else minCoins
            