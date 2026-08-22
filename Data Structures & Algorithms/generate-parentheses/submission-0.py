class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sub, cursub = [], []

        def helper(n, openp, closep): 
            if openp == closep == n: 
                sub.append("".join(cursub))
                return
            
            if openp < n :
                cursub.append("(")
                helper(n, openp+1, closep)
                cursub.pop()
            if closep < openp:
                cursub.append(")") 
                helper(n, openp, closep+1)
                cursub.pop()

        helper(n,0,0)
        return sub
                
            

            
        