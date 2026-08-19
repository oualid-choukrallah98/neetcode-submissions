class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L = 0
        R = len(matrix) - 1
        row = -1
        while L <= R:
            mid = (L+R)//2
            if target < matrix[mid][0]  : 
                R = mid -1
            elif target > matrix[mid][-1] :
                L = mid + 1
            else : 
                row = mid 
                break
        if row == -1 : 
            return False 

        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            mid2 = (l+r)//2
            if matrix[row][mid2] < target:
                l = mid2 + 1
            elif matrix[row][mid2] > target:
                r = mid2 -1
            else : 
                return True 
        return False 

       
        