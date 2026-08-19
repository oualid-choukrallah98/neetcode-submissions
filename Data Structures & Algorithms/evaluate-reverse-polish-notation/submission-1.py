class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens: 
            if token == "+" : 
                a = stack.pop()
                b = stack.pop()
                add = a + b
                stack.append(add)
            elif token == "*":
                a = stack.pop()
                b = stack.pop()
                mult = a * b
                stack.append(mult)
            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                minus = b - a
                stack.append(minus)
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                div = int(b / a)
                stack.append(div)
            else : 
                stack.append(int(token))
        return stack[-1]
                

        