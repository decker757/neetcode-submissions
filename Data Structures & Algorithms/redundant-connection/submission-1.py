class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
            Graph has a cycle and we need to identify the edge to remove
                - Have to check if there's a cycle
                    - is there more than 1 cycle?
                    - if yes, find remove the last detected cycle

            DFS -> build adjList both directions, check for cycles by iterating through the adjList recursively.
        """

        adjList = {i: [] for i in range(1, len(edges) + 1)}
        def dfs(node, parent, visited):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adjList[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node, visited):
                    return False
            return True

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            if not dfs(u, -1, set()):
                return [u, v]

