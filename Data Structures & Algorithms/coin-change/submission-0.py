class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0: 0}

        def dfs(remaining):
            if remaining in memo : 
                return memo[remaining]

            if remaining <0 : 
                return float('inf')
            
            res = float('inf')

            for coin in coins: 
                num_coins = dfs(remaining - coin)
                res = min(res, 1+ num_coins)

            memo[remaining] = res
                
            
            return res
        
        result = dfs(amount)
        # If result is still infinity, it means no combination worked
        return result if result != float('inf') else -1