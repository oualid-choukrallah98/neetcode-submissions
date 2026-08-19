class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            for number in row: 
                if number == target:
                    return True
        return False
        