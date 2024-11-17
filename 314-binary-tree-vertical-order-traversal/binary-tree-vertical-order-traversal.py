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
        # hash mapy will store keys -> column, values -> node values
        columnTable = defaultdict(list)
        # min and max column will be used for range when returning answer
        min_column = max_column = 0
        # make DFS helper
        def DFS(node, row, column):
            if node:
                # add nonlocal to be able to modify the min and max gloabl variables
                nonlocal min_column, max_column
                # process the current node by appending the (row, node value) in column key
                columnTable[column].append((row, node.val))
                # update min column
                min_column = min(min_column, column)
                # do the same for max column
                max_column = max(max_column, column)

                # preorder traveral (can use inorder or postorder as well)
                DFS(node.left, row + 1, column - 1)
                DFS(node.right, row + 1, column + 1)
        # being DFS
        DFS(root, 0, 0)
        # sort each (row, node value) tuple for each of their respective column key in hashtable
        res = []
        for col in range(min_column, max_column + 1):
            # sort the column key by row which is the first position in each tuple
            columnTable[col].sort(key=lambda x:x[0])
            # collect the values
            colVals = [val for _, val in columnTable[col]]
            res.append(colVals)

        return res
                








