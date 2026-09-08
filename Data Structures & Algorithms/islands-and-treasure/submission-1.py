class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visited = set()

        def addland(r,c): 
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited or grid[r][c] == -1:
                return 
            q.append((r,c))
            visited.add((r,c))

        for r in range(rows):
            for c in range(cols): 
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        distance = 0 
        while q: 
            for i in range(len(q)):
                row, column = q.popleft()
                grid[row][column] =  distance 
                addland(row+1,column)
                addland(row,column+1)
                addland(row-1,column)
                addland(row,column-1)
            
            distance += 1
                    

            


            
        