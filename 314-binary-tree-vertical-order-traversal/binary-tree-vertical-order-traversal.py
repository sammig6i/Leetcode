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

        def DFS(node, row, column):
            if node:
                nonlocal min_column, max_column
                DFS(node.left, row + 1, column - 1)
                columnTable[column].append((row, node.val))
                min_column = min(min_column, column)
                max_column = max(max_column, column)
                DFS(node.right, row + 1, column + 1)
        
        DFS(root, 0, 0)

        res = []
        for col in range(min_column, max_column + 1):
            columnTable[col].sort(key=lambda x:x[0])
            colVals = [val for row, val in columnTable[col]]
            res.append(colVals)

        return res
                








