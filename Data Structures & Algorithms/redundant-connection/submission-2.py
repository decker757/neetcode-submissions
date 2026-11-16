class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = {i: [] for i in range(1, len(edges) + 1)}

        def dfs(node, parent, visited):
            if node in visited:
                return False
            
            visited.add(node)
            
            for nei in adjList[node]:
                if nei == parent:
                    continue
                elif not dfs(nei, node, visited):
                    return False
            return True

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

            if not dfs(u, -1, set()):
                return [u, v]

