class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        trf_map = {}

        for payer, payee, amt in transactions:
            trf_map[payer] = trf_map.get(payer, 0) - amt
            trf_map[payee] = trf_map.get(payee, 0) + amt
        
        balances = tuple(amt for amt in trf_map.values() if amt != 0)
        memo = {}
        def dfs(curr_balance):
            state = tuple(sorted(curr_balance))

            if state in memo:
                return memo[state]

            if all(bal == 0 for bal in curr_balance):
                return 0
            
            min_transactions = float('inf')

            for i in range(len(curr_balance)):
                if curr_balance[i] < 0:
                    for j in range(len(curr_balance)):
                        if curr_balance[j] > 0:
                            settle = min(abs(curr_balance[i]), curr_balance[j])
                            new_balances = list(curr_balance)
                            new_balances[i] += settle
                            new_balances[j] -= settle

                            min_transactions = min(min_transactions, 1 + dfs(tuple(new_balances)))
                
            memo[state] = min_transactions
            return min_transactions

        return dfs(balances)