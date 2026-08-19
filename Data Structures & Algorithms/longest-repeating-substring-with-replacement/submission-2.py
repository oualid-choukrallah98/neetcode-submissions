class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      count = {}
      L = 0
      R = 0
      maxfreq = 0
      res = 1

      for R in range(len(s)):
        count[s[R]] = count.get(s[R],0) + 1
        maxfreq = max(count.values())
        if (R - L)+1 - maxfreq > k:
            count[s[L]] -= 1
            L += 1
        res = max(res,(R - L)+1)
      return res


#[A,B,A,C,C,A]
#K = 2
#MAX FREQ = 1


        


        
        


        

        