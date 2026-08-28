class Solution:
    def countSubstrings(self, s: str) -> int:
        output = 0 
        #odd substring
        for i in range(len(s)): 
            l,r = i,i
            while l >= 0 and r <len(s) and s[l] == s[r] :
                l -= 1
                r += 1
                output +=1
            
        
        #even substring 
        for i in range(len(s)-1): 
            l, r = i, i+1
            while  l >= 0 and r <len(s) and s[l] == s[r] :
                l -= 1
                r += 1
                output +=1


        return output 



        