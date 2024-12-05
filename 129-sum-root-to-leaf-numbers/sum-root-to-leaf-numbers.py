# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 0]]
        res = 0

        while stack:
            node, num = stack.pop()
            if node:
                num = num * 10 + node.val
                if not node.left and not node.right:
                    res += num
                else:
                    stack.append([node.left, num])
                    stack.append([node.right, num])
        return res