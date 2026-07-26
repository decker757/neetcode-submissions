# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ls = []
        smallest = None
        if not root:
            return None
        
        self.dfs(root, ls)
        i = 0
        while i < k:
            smallest = ls[i]
            i += 1
        return smallest
            
        
    def dfs(self, node, res):
        if not node:
            return None

        self.dfs(node.left, res)
        res.append(node.val)
        self.dfs(node.right, res)
