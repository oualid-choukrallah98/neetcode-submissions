class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        r = 0
        result = 0
        maxfreq = 0
        while r <= len(s) - 1:
            count[s[r]] = count.get(s[r], 0) + 1      
            maxfreq = max(maxfreq, count[s[r]])       
            lenght = r - l + 1
            if lenght - maxfreq <= k :
                result = max(result, lenght)
        
            else : 
                count[s[l]] -= 1
                l += 1
            r += 1
        return result


        
        


        

        