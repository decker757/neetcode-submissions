class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}
        for cou, pre in prerequisites:
            adjList[cou].append(pre)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if adjList[course] == []:
                return True

            visited.add(course)
            for nei in adjList[course]:
                if not dfs(nei):
                    return False
            visited.remove(course)
            adjList[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True