# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        depth = 0
        q = deque([root])

        while q:
            ls = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    ls.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if ls:
                res.append(ls)
        return res