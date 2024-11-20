# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        if not root:
            return 0
        
        depth = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    if node.right: q.append(node.right)
                    if node.left: q.append(node.left)
            depth += 1

        return depth


        
        


       

        
        
        