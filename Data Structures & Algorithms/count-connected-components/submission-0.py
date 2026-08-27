class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mapping = {i : [] for i in range(n)}
        for node, neigh in edges: 
            mapping[node].append(neigh)
            mapping[neigh].append(node)
        
        visited = set()
        nb_components = 0

        def dfs(node): 
            visited.add(node)
            for neigh in mapping[node]: 
                if neigh not in visited: 
                    dfs(neigh)

            
        
        for i in range(n): 
            if i not in visited: 
                dfs(i)
                nb_components += 1 
        return nb_components

        