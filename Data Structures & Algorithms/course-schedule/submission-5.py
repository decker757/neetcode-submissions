class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}

        for cou, prereq in prerequisites:
            adjList[cou].append(prereq)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if adjList[course] == []:
                return True
            
            visited.add(course)
            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False
            adjList[course] = []
            visited.remove(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True