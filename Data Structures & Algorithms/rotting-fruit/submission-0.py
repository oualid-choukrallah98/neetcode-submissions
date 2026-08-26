class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()
        fresh = 0 
        def addbanana(r,c): 
            nonlocal fresh
            if r< 0 or c < 0 or r>= rows or c>= cols or (r,c) in visited or  grid[r][c] != 1: 
                return 
            q.append((r,c))
            visited.add((r,c))
            fresh -= 1

        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 2: 
                    q.append((r,c))
                    visited.add((r,c))
                if grid[r][c] == 1: 
                    fresh += 1
        
        minute = 0 
        while q and fresh >0 : 
            for i in range(len(q)): 
                r, c  = q.popleft()
                grid[r][c] = 2
                neighbors = [[0,1], [1,0], [0,-1], [-1,0]]
                for nr, nc in neighbors: 
                    addbanana(r+nr, c+ nc)
            minute += 1
        
        return minute if fresh == 0 else -1
        