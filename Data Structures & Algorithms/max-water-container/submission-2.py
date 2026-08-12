class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume = (len(heights) -1) * min(heights[0] , heights[len(heights)-1] )
        L = 0 
        R = len(heights) - 1
        while L < R : 
            if heights[L] <= heights[R] : 
                L += 1
                volume = (R-L) * min(heights[L] , heights[R] )
                max_volume = max(max_volume, volume)
            else :
                R -= 1
                volume = (R-L) * min(heights[L] , heights[R] )
                max_volume = max(max_volume, volume)
        return max_volume


        
        