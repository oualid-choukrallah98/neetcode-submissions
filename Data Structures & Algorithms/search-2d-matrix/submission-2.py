class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        for i in range(rows-1,-1,-1):
            if target < matrix[i][0]:
                continue
            elif target > matrix[i][0] :
                column = matrix[i]
                l = 0
                r = len(column) - 1 
                while l <= r :
                    mid = (l+r) // 2 
                    if target < column[mid]:
                        r = mid - 1 
                    elif target > column[mid]:
                        l = mid + 1 
                    else : 
                        return True
                return False 
            else :
                return True 
        return False
                

                


            

        