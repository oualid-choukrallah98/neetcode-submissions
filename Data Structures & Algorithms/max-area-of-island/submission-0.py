class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: 
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        island = 0 
        result = 0 
         
        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            island_size = 1
            while q:
                row, col = q.popleft()
                directions = [[0,1],[1,0],[-1,0],[0,-1]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r in range(rows) and c in range(cols) and (r,c) not in visited
                     and grid[r][c] == 1):
                        q.append((r,c))
                        visited.add((r,c))
                        island_size += 1
            return island_size
                


        for row in range(rows): 
            for col in range(cols):
                if grid[row][col] == 1 and (row,col) not in visited:
                    size = bfs(row,col)
                    island += 1
                    result = max(result, size)

        return result
        