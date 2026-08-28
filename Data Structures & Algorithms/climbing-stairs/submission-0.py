class Solution:
    def climbStairs(self, n: int) -> int:
        first = 0
        second = 1
        for i in range(n): 
            variable = second
            second = first + second
            first = variable
        
        return second 
