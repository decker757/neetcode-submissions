class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
            What we know:
                1. undirected graph
                2. no repeated edges therefore no cycles
            
            Approach:
                1. build adjList, both directions
                2. perform dfs(node) if reached end, add 1 to res
                3. since there are no cycles as there are no repeated edges, no need set
        """

        adjList = {i: [] for i in range(n)}
        res = 0
        visited = set()
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        def dfs(node):
            visited.add(node)
            for nei in adjList[node]:
                if nei not in visited:
                    dfs(nei)

        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1

        return res
        