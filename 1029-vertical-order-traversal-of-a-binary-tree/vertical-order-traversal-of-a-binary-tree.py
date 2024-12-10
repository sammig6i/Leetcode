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
        
        q = deque([(root, 0, 0)])
        d = defaultdict(list)

        min_col = max_col = 0

        while q:
            node, row, col = q.popleft()
            if node:
                d[col].append([node.val, row])

                min_col = min(min_col, col)
                max_col = max(max_col, col)

                q.append([node.left, row + 1, col - 1])
                q.append([node.right, row + 1, col + 1])
        
        res = []
        for col in range(min_col, max_col + 1):
            d[col].sort(key=lambda x: (x[1], x[0]))
            vals = [v for v, _ in d[col]]
            res.append(vals)
        return res


