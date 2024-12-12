# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root, p, q):
            if not root:
                return None
            
            if root == p or root == q:
                return root
            
            L = dfs(root.left, p, q)
            R = dfs(root.right, p, q)

            return root if L and R else L or R
        
        return dfs(root, p, q)