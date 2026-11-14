# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
            1. Level order traversal
            2. Add the nodes from left to right into an array
            3. Append this array to another array to track what nodes we have at each Level
            4. Iterate through this array, return the last element of each level
        """
        if not root:
            return []

        level_ls = []
        q = deque([root])

        while q:
            depth_ls = []
            for _ in range(len(q)):
                node = q.popleft()

                depth_ls.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level_ls.append(depth_ls)

        res = []
        for d in level_ls:
            res.append(d[-1])
        return res

