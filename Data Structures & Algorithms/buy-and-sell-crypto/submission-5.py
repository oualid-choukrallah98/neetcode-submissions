class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        L = 0 
        R = 1
        while R <= len(prices) - 1:
            if prices[L] < prices[R]:
                profit = prices[R] - prices[L]
                result = max(result, profit)
            else : 
                L = R
            R = R + 1    
        return result 
                

        