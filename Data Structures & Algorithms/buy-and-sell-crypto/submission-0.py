class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices)-1, -1, -1):
            for j in range(max(i-1,0), -1, -1):
                profit = prices[i] - prices[j]
                result = max(result, profit)
        return result

        