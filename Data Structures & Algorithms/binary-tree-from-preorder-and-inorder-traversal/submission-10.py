# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hm = {}
        for i, n in enumerate(inorder):
            hm[n] = i
        
        self.preorder_pointer = 0

        def dfs(l, r):
            if l > r:
                return None
            
            root_val = preorder[self.preorder_pointer]
            self.preorder_pointer += 1
            root = TreeNode(root_val)

            root_idx = hm[root_val]
            root.left = dfs(l, root_idx - 1)
            root.right = dfs(root_idx + 1, r)

            return root
        
        return dfs(0, len(inorder) - 1)

        

