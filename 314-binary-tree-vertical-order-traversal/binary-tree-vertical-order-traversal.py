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
        if not root:
            return []
        
        while q:
            node, column = q.popleft()
            if node:
                d[column].append(node.val)
                q.append((node.left, column - 1))
                q.append((node.right, column + 1))
        return [v for _, v in sorted(d.items())]





