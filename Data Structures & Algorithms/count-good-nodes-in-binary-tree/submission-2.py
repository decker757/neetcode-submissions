# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
            Definition of a good note:
                - if no node from the root to X is greater than X
                  then it is a good node.
            
            So intuitively, we can think of it as doing a post order traversal,
            then once we gather the left and right subtrees, we can check if there is any
            node that is greater than the node from before.

            So 2 conditions to count:
                1. node must be greater than root
                2. everything inbetween must be smaller than root
        """
        def dfs(node, max_value):
            if not node:
                return 0
            
            count = 0

            if node.val >= max_value:
                count = 1

            max_value = max(max_value, node.val)

            count += dfs(node.left, max_value)
            count += dfs(node.right, max_value)

            return count
        
        return dfs(root, root.val)
    

