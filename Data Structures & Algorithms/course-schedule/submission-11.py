class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}
        visited = set()

        for pre, cou in prerequisites:
            adjList[cou].append(pre)
        
        def dfs(course):
            if course in visited:
                return False
            if adjList[course] == []:
                return True
            
            visited.add(course)
            for pre in adjList[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            adjList[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        