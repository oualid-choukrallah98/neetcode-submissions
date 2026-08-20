class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)
        for index, value in enumerate(temperatures):
            while stack and temperatures[index] > stack[-1][0]:
                stack_t, stack_i = stack.pop()
                output[stack_i] = index - stack_i

            stack.append([value,index])
            
        return output 
            





    






