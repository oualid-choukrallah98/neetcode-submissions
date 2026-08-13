class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles): 
            return max(piles)


        l = 1
        r = max(piles)
        mid = (l+r)// 2
        res = max(piles)

        while l <= r : 
            mid = (l+r)// 2
            rate = 0 
            for num in piles : 
                rate += math.ceil(num / mid)

            if rate <= h :
                res = min(res,mid)
                r = mid -1
            else  :
                l = mid + 1


        return res
                

        