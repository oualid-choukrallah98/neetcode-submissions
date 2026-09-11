class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        path = set()
        island = 0 
        def dfs(r,c): 
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in path or grid[r][c] == "0": 
                return 
            path.add((r,c))
            for (nr, nc) in ((0,1),(1,0),(0,-1),(-1,0)):
                dfs(r+nr, c+nc)
            
        
        for row in range(rows): 
            for col in range(cols): 
                if grid[row][col] == "1" and (row, col) not in path:
                    dfs(row,col)
                    island += 1
        
        return island 
        


        