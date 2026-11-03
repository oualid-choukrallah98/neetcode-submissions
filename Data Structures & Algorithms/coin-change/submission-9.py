class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(remaining): 
            if remaining in memo: 
                return memo[remaining]
            if remaining == 0: 
                return 0 
            elif remaining < 0: 
                return False 
            res = float('inf')
            for coin in coins: 
                if remaining - coin >= 0:
                    res = min(res,1 + dfs(remaining - coin))
            
            memo[remaining] = res
            return res

        mincoins = dfs(amount)
        return -1 if  mincoins == float('inf') else mincoins
        

            

            
        