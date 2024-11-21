# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 1)])
        max_depth = 0
        if not root:
            return 0
        
        while q:
            for i in range(len(q)):
                node, level = q.popleft()
                
                if node:
                    max_depth = max(level, max_depth)
                    q.append([node.left, level + 1])
                    q.append([node.right, level + 1])
        return max_depth


        
        