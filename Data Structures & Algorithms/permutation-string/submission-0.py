class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0 
        count_s1 = {}
        for l in s1 : 
            count_s1[l] = count_s1.get(l,0) + 1
        l = 0 
        r = l+len(s1)-1
        while r< len(s2): 
            count_s2 = {}
            for i in range(l,r+1):
                char = s2[i]
                count_s2[char] = count_s2.get(char,0) + 1

            if count_s2 == count_s1:
                return True
            else : 
                l += 1
                r += 1
        return False 


        