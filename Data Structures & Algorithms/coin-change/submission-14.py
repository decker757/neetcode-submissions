class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(a):
            if a <= 0:
                return 0
            if a in memo:
                return memo[a]
            res = amount + 1
            for c in coins:
                if a - c >= 0:
                    res = min(dp(a - c) + 1, res)
            memo[a] = res
            return memo[a]

        minCoins = dp(amount)

        return -1 if minCoins >= amount + 1 else minCoins
            