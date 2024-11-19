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
        res = []
        max_column = min_column = 0
        if not root:
            return []

        while q:
            node, column = q.popleft()
            if node:
                d[column].append(node.val)
                q.append([node.left, column - 1])
                q.append([node.right, column + 1])
                max_column = max(max_column, column)
                min_column = min(min_column, column)
        return [d[v] for v in range(min_column, max_column + 1)]

        


