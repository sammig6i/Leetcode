# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return self.dfs(root, 0)

    def dfs(self, node, num):
        if not node:
            return 0
        
        num = num * 10 + node.val
        if not node.left and not node.right:
            return num
        
        return self.dfs(node.left, num) + self.dfs(node.right, num)