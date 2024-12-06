# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        self.res = []

        return self.dfs(root, 0)

    def dfs(self, node, depth):
        if not node:
            return None
        
        if len(self.res) == depth:
            self.res.append(node.val)
        
        self.dfs(node.right, depth + 1)
        self.dfs(node.left, depth + 1)

        return self.res

