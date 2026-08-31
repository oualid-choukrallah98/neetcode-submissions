class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxrate = max(piles)
        l = 1
        r = maxrate
        rate = maxrate
        while l <= r: 
            mid = (l+r)//2
            count = 0
            for pile in piles: 
                count += math.ceil(pile/mid)
            if count <= h :
                rate = min(rate,mid)
                r = mid -1
            else : 
                l = mid + 1
        return rate

        



