class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        
        l = 1
        r = max(piles)
        result = r
        while l < r:
            mid = (l+r)//2
            rate = 0
            for i in range(len(piles)):
                rate += (piles[i]+mid-1)//mid
            if rate > h :
                l = mid + 1
            else :
                resultat = mid
                r = mid
            result = min(result, rate)
        return resultat
            
        
        
        
        