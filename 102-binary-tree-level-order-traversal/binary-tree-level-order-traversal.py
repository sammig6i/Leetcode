# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        def dfs(node, depth):
            if not node:
                return None
            
            if len(res) == depth:
                res.append([])
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            res[depth].append(node.val)
        
        dfs(root, 0)
        return res
