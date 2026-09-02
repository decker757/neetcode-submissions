class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo = [[-1] * (amount + 1) for _ in range(len(coins))]
        
        def dp(i, a):
            if a == 0:
                return 1
            if i >= len(coins):
                return 0
            if memo[i][a] != -1:
                return memo[i][a]

            res = 0
            if a - coins[i] >= 0:
                res = dp(i + 1, a)
                res += dp(i, a - coins[i])
            memo[i][a] = res
            return res
        
        return dp(0, amount)