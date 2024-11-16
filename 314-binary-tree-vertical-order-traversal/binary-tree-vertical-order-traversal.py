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

        columnTable = defaultdict(list)
        min_column = max_column = 0
        q = deque([(root, 0)])


        while q:
            node, column = q.popleft()
            if node:
                columnTable[column].append(node.val)
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                q.append((node.left, column - 1))
                q.append((node.right, column + 1))
        return [columnTable[v] for v in range(min_column, max_column + 1)]








