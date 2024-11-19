# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        q = deque([(root, 0)])
        min_column = max_column = 0
        if not root:
            return []

        while q:
            node, col = q.popleft()
            if node:
                d[col].append(node.val)
                q.append([node.left, col - 1])
                q.append([node.right, col + 1])
                min_column = min(min_column, col)
                max_column = max(max_column, col)

        return [d[v] for v in range(min_column, max_column + 1)]
