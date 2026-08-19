class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_rate = max(piles)
        L = 1
        R = max_rate
        res = R
        while L <= R :
            mid = (L+R) // 2
            hours = 0
            for pile in piles : 
                hours += math.ceil(pile/mid)
            if hours <= h :
                res = mid 
                R = mid -1
            elif hours > h:
                L = mid + 1
            
        return res




    
  

    