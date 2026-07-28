# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False
            
        def isSameTree(root, subroot):
            q1 = deque([root])
            q2 = deque([subroot])

            while q1 and q2:
                for _ in range(len(q1)):
                    node1 = q1.popleft()
                    node2 = q2.popleft()
                    if not node1 and not node2:
                        continue

                    if not node1 or not node2 or node1.val != node2.val:
                        return False
                    
                    q1.append(node1.left)
                    q1.append(node1.right)
                    q2.append(node2.left)
                    q2.append(node2.right)

            return True
        
        if isSameTree(root, subRoot):
            return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
