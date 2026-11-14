# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
            we have the root, p, q
                - they do not necessarily need to be on different subtrees from the root
                - a parent node can also be p which makes it possible for the parent to be the LCA
            
            Because this is a BST:
                1. left subtree < right subtree
                2. It is also a CBT
            This gives rise to 3 cases
                1. p.val < root.val < q.val
                2. max(p.val, q.val) < root.val
                3. min(p.val, q.val) > root.val

            1 base case -> if not root return None
        """
        cur = root

        while cur:
            if min(p.val, q.val) > cur.val:
                cur = cur.right
            elif max(p.val, q.val) < cur.val:
                cur = cur.left
            else:
                return cur