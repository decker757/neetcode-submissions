class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i: [] for i in range(n)}
        visited = set()
        res = 0

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for nei in adjList[node]:
                if nei not in visited:
                    dfs(nei)
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res
        