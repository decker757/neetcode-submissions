"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        if not node:
            return None

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            root = Node(node.val)
            oldToNew[node] = root 
            for n in node.neighbors:
                root.neighbors.append(dfs(n))
            
            return root

        return dfs(node)