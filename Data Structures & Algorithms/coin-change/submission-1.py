class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0: 0}

        def dfs(remaining): 
            if remaining in memo: 
                return memo[remaining]
            if remaining < 0: 
                return float('inf')

            res = float('inf')
            
            for coin in coins:
                numb_coins = dfs(remaining - coin)
                res = min(numb_coins+1, res)

            memo[remaining] = res
            return res 
        
        return dfs(amount) if dfs(amount) != float("inf") else -1
                
            

