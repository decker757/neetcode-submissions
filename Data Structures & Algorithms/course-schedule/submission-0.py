class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = { i : [] for i in range(numCourses)}
        visitSet = set()

        for course, prereq in prerequisites:
            adj[course].append(prereq)

        def dfs(course):
            if course in visitSet:
                return False
            
            if adj[course] == []:
                return True
            
            visitSet.add(course)
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            visitSet.remove(course)
            adj[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
