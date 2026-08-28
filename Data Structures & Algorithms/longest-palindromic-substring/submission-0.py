class Solution:
    def longestPalindrome(self, s: str) -> str:
        biggest = ""
        lenght = 0
        #odd numbers 
        for i in range(len(s)): 
            l,r = i,i
            while l>=0 and r < len(s) and s[l] == s[r]: 
                if lenght <= r-l+1: 
                    biggest = s[l:r+1] 
                    lenght = max(lenght, r-l+1)
                l -=1
                r += 1
            
        
        #even numbers
        for i in range(len(s)): 
            l,r = i,i+1
            while l>=0 and r < len(s) and s[l] == s[r]: 
                if lenght <= r-l+1: 
                    biggest = s[l:r+1] 
                    lenght = max(lenght, r-l+1)
                l -=1
                r += 1
        
        return biggest
