class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i: [] for i in range(numCourses)}

        for cou, pre in prerequisites:
            adjList[cou].append(pre)

        visited = set()
        done = set()
        res = []

        def dfs(course):
            if course in visited:
                return False
            if course in done:
                return True
            
            visited.add(course)
            for pre in adjList[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            done.add(course)
            res.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []

        return res
