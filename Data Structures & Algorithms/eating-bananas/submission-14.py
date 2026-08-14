class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_rate = max(piles)
        L = 1
        R = max_rate 
        rate = max_rate
        while L <= R:
            mid = (L+R)//2
            count = 0
            for num in piles : 
                count += math.ceil(num/mid)
            if count <= h :
                rate = min(rate,mid)
                R = mid -1
            else : 
                L = mid + 1
        return rate

        

        
            
            


            

        