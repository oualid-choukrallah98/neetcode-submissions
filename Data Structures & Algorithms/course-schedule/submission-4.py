class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {i: [] for i in range(numCourses)}
        for c, p in prerequisites: 
            courses[c].append(p)
        
        visited = set()
        def dfs(course):
            if course in visited: 
                return False
             
            if courses[course] == []: 
                return True
            
            visited.add(course)
            for i in range(len(courses[course])): 
                if not dfs(courses[course][i]):
                    return False 
                
            visited.remove(course)
            courses[course] = []
            return True 
        
        for i in range(numCourses): 
            if not dfs(i): 
                return False 
        
        return True 
        



        