class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l_row = 0 
        r_row = rows - 1
        mid = (l_row +r_row) // 2
        row = -1
        while l_row <= r_row :
            if matrix[mid][-1] < target:
                l_row = mid + 1
                mid = (l_row +r_row) // 2
                

            elif matrix[mid][0] > target:
                r_row = mid - 1 
                mid = (l_row +r_row) // 2
            
            else : 
                row = matrix[mid]
                break
        if row == -1:
            return False
        l_col = 0
        r_col = cols - 1
        mid = (l_col +r_col) // 2
        while l_col <= r_col : 
            if row[mid] < target:
                l_col = mid + 1 
                mid = (l_col +r_col) // 2
            elif row[mid] > target:
                r_col = mid - 1 
                mid = (l_col +r_col) // 2
            else :
                return True
        return False



                
            
                



        