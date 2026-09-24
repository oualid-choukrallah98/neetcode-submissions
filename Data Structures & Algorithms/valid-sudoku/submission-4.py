class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)
        for  r in range(9): 
            for c in range(9): 
                if board[r][c] == "." :
                    continue
                elif board[r][c] not in row[r] and board[r][c] not in col[c] and board[r][c] not in square[(r//3,c//3)]:
                    row[r].add(board[r][c])
                    col[c].add(board[r][c])
                    square[(r//3,c//3)].add(board[r][c])

                else:
                    return False
        
        return True

        

                   
                    
