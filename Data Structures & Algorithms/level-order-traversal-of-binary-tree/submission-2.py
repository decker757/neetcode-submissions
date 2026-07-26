# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = deque()
        q.append(root)

        while q:
            ls = []
            n = len(q)

            for i in range(n):
                node = q.popleft()
                if node:
                    ls.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            res.append(ls) if len(ls) > 0 else None
        return res