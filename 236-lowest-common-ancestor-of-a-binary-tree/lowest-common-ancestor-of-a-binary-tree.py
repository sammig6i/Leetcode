# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)
    
    def dfs(self, node, p, q):
        if not node:
            return None
        
        
        L = self.dfs(node.left, p, q)
        R = self.dfs(node.right, p, q)
        if node == p or node == q:
            return node

        return node if L and R else L or R

