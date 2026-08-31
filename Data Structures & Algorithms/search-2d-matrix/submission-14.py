class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        # Detect the right row 
        l_row = 0
        r_row = row -1
        while l_row <= r_row: 
            mid_row = (l_row + r_row)//2
            if target < matrix[mid_row][0]: 
                r_row = mid_row -1
            elif target > matrix[mid_row][-1]: 
                l_row = mid_row + 1
            
            else : 
                break
        # verify the target in the right row 
        l_col = 0
        r_col = col -1
        while l_col <= r_col: 
            mid_col = (l_col + r_col)//2
            if target < matrix[mid_row][mid_col]:
                r_col -= 1
            elif target > matrix[mid_row][mid_col]:
                l_col += 1
            else : 
                return True 

        return False 



        
            
        

        