class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for index, value in enumerate(temperatures):
            while stack and value > stack[-1][1]: 
                i, t = stack.pop()
                result[i] = index - i
            
            stack.append((index,value))
        
        return result 