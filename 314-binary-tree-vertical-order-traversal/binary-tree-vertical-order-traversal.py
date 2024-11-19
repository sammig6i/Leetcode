# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        min_column = max_column = 0
        d = defaultdict(list)
        if not root:
            return []

        def dfs(node, row, col):
            nonlocal min_column, max_column
            if node:
                d[col].append((row, node.val))
                min_column = min(min_column, col)
                max_column = max(max_column, col)
                dfs(node.left, row + 1, col - 1)
                dfs(node.right, row + 1, col + 1)
        
        dfs(root, 0, 0)
        res = []
        for col in range(min_column, max_column + 1):
            d[col].sort(key=lambda x: x[0])
            cols = [v for _, v in d[col]]
            res.append(cols)
        return res
    
    
