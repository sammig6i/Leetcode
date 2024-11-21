# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        res = []
        if not root:
            return res

        while q:
            max_node = float("-inf")
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    max_node = max(node.val, max_node)
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
            res.append(max_node)
        return res
