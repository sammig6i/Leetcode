# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        q = deque([root])
        total_sum = 0

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    if low <= node.val <= high:
                        total_sum += node.val
                    q.append(node.left)
                    q.append(node.right)
        return total_sum
