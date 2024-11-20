# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root:
                return 0
            
            return 1 + max(dfs(root.right, depth + 1), dfs(root.left, depth + 1))
            
            
            
        
        return dfs(root, 1)

        
        


       

        
        
        