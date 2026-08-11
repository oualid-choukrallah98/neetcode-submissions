class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        L = 0
        R = len(s) - 1
        while L < R :
            if s[L] == s[R] : 
                L += 1
                R -= 1
            else : 
                return False 
        return True 

        