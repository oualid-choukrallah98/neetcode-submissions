class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        result = r
        while l < r:
            mid = (l + r) // 2 
            hours = 0 
            for i in range (len(piles)):
                hours += (mid + piles[i] - 1) // mid
            if hours > h :
                l = mid + 1
            else : 
                r = mid 
        return l
            
            


        