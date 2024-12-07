# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        
        self.d = defaultdict(list)
        self.min_col = self.max_col = 0

        self.dfs(root, 0, 0)
    
        res = []
        for col in range(self.min_col, self.max_col + 1):
            self.d[col].sort(key=lambda x: (x[1], x[0]))
            vals = [v for v, _ in self.d[col]]
            res.append(vals)
        return res

    def dfs(self, node, row, col):
        if not node:
            return None

        self.d[col].append([node.val, row])

        self.min_col = min(self.min_col, col)
        self.max_col = max(self.max_col, col)

        self.dfs(node.right, row + 1, col + 1)
        self.dfs(node.left, row + 1, col - 1)

        