class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        for c, pre in prerequisites:
            courses[c].append(pre)

        visited = set()
        def dfs(course): 
            if course in visited: 
                return False
            if courses[course] == []:
                return True
            
            visited.add(course)
            for p in courses[course]: 
                if not dfs(p): 
                    return False 
            visited.remove(course)
            courses[course] = []
            return True 
            
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True  


        