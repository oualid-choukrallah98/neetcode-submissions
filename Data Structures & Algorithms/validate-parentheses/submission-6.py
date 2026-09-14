class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")": "(", "]": "[", "}": "{"}
        stack = []
        for p in s : 
            if p not in hashmap: 
                stack.append(p)
            else : 
                if stack and stack[-1] == hashmap[p]: 
                    stack.pop()
                else : 
                    return False
                
        return True if not stack else False
        

       

        