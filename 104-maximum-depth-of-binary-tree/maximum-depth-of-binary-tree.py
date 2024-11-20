# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def dfs(root, depth):
            nonlocal max_depth
            if not root:
                return 0
            
            max_depth = max(depth, max_depth)

            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
            return max_depth

        return dfs(root, 1)

        
        


       

        
        
        