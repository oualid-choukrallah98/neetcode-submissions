class MinStack:

    def __init__(self):
        self.stack = []
        self.stackmin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.stackmin[-1]) if self.stackmin else val
        self.stackmin.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.stackmin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stackmin[-1]
        
