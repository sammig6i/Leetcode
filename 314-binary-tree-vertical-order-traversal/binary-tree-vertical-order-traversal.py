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

        d = defaultdict(list)
        min_column = max_column = 0
        q = deque([(root, 0)])

        while q:
            node, col = q.popleft()
            if node:
                d[col].append(node.val)
                min_column = min(min_column, col)
                max_column = max(max_column, col)
                q.append((node.left, col - 1))
                q.append((node.right, col + 1))
        return [d[v] for v in range(min_column, max_column + 1)]