class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(i):
            if i <= 0:
                return 0

            if i in memo:
                return memo[i]

            res = amount + 1
            for c in coins:
                if i - c >= 0:
                    res = min(res, dp(i - c) + 1)
            memo[i] = res
            return memo[i]
        
        minChange = dp(amount)

        return -1 if minChange >= amount + 1 else minChange 