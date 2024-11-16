# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([(root, 0)])
        d = defaultdict(list) # keys - column, values - nodes

        if not root:
            return []

        while q:
            for i in range(len(q)):
                node, column = q.popleft()
                if node:
                    d[column].append(node.val)
                    q.append((node.left, column - 1))
                    q.append((node.right, column + 1))
        return [v for _, v in sorted(d.items())]





