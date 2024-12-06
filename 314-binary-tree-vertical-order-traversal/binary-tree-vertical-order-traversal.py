# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        self.d = defaultdict(list)
        self.min_col = self.max_col = 0

        self.dfs(root, 0, 0)

        res = []
        for c in range(self.min_col, self.max_col + 1):
            self.d[c].sort(key=lambda x: x[0])
            vals = [v for _, v in self.d[c]]
            res.append(vals)
        return res

       

    def dfs(self, node, r, c):
        if not node:
            return None
        
        self.d[c].append((r, node.val))

        self.min_col = min(self.min_col, c)
        self.max_col = max(self.max_col, c)

        self.dfs(node.left, r + 1, c - 1)
        self.dfs(node.right, r + 1, c + 1)


        
        

