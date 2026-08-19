class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0 
        L = 0
        R = 1
        while R <= len(prices)-1:
            profit = 0 
            if prices[L] >= prices[R]:
                L  = R
                R += 1
            else : 
                profit = prices[R] - prices[L]
                result = max(profit,result)
                R += 1
        return result






       
                




        

        



