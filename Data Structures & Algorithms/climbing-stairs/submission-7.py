class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 1
        for _ in range(n-1):
            variable = first
            first = first + second
            second = variable
        
        return first 
        