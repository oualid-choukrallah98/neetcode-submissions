class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        for index, value in enumerate(temperatures):
            while stack and value > stack[-1][0]: 
                stackt, stacki = stack.pop()
                output[stacki] = index - stacki
            stack.append([value, index])
        
        return output
                
            

             
            







        