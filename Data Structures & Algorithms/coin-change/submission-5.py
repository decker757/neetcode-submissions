class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(i):
            if i <= 0:
                return 0

            if i in memo:
                return memo[i]
            
            res = 1e9
            for c in coins:
                if i - c >= 0:
                    res = min(res, 1 + dp(i - c))
            memo[i] = res
            return memo[i]
        
        minCoins = dp(amount)

        return -1 if minCoins >= 1e9 else minCoins