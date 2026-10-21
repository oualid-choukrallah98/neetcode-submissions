class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {i: [] for i in range(numCourses)}
        for i, j in prerequisites: 
            prereq[i].append(j)
            
        visitset = set()

        def dfs(i): 
            if i in visitset: 
                return False 
            if prereq[i] == []: 
                return True
            visitset.add(i)
            for crs in prereq[i]:
                if not dfs(crs): 
                    return False 

            visitset.remove(i)
            prereq[crs] = []
            return True 
        
        for crs in range(numCourses): 
            if not dfs(crs): 
                return False 
        return True 

            
            
            
        
        