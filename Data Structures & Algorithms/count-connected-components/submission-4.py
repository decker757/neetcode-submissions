class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i: [] for i in range(n)}
        visited = [False] * n
        res = 0

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        def dfs(node):
            for nei in adjList[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
        
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i) 
                res += 1

        return res
                