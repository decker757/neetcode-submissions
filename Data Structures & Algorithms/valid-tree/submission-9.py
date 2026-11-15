class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
            what we know:
                1. undirected graph so it can go both directions
                2. A valid tree does not have cycles
            
            approach:
                1. create adjList for both directions
                2. dfs -> check if node is in visited set to detect cycles
                            - if cycle detected, return False
                            - have to skip parent node if parent has been previously visited
                            - if adjList reached end, return True
        """
        if n < len(edges):
            return False

        adjList = {i: [] for i in range(n)}

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adjList[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        if not dfs(0, -1):
            return False
        return len(visited) == n


