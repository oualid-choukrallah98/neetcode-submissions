class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hashmap = {i: [] for i in range(n)}
        for node1, node2 in edges:
            hashmap[node1].append(node2)
            hashmap[node2].append(node1)
        
        visited = set()
        def dfs(node, parent): 
            if node in visited: 
                return False 
            
            visited.add(node)
            
            for neigh in hashmap[node]: 
                if neigh == parent: 
                    continue

                if not dfs(neigh,node) : return False 

            return True 
        
    
        
        return dfs(0, -1) and len(visited) == n
            


        