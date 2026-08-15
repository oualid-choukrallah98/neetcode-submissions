class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seti = set()
        longest = 0
        for r in range(len(s)):
            while s[r] in seti : 
                seti.remove(s[l])
                l += 1
            seti.add(s[r])
            longest = max(longest, r-l+1)
        return longest 
         
            


        