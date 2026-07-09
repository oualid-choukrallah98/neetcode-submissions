class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0]) 

        l_row = 0
        r_row = rows - 1
        while l_row  <= r_row :
            mid = (l_row + r_row) // 2
            if target < matrix[mid][0]:
                r_row = mid - 1
            elif target > matrix[mid][-1] :
                l_row = mid + 1
            else:
                break
        if not (l_row<=r_row):
            return False 
        row  = (l_row + r_row) // 2
        l_col = 0
        r_col = cols - 1 
        while l_col <= r_col:
            mid = (l_col + r_col) // 2
            if target < matrix[row][mid]:
                r_col = mid -1
            elif target > matrix[row][mid]:
                l_col = mid + 1
            else :
                return True
        return False





