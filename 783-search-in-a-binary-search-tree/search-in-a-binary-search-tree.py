# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return root

        if val > root.val:
            return self.searchBST(root.right, val)
            res.append(root.right)
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return root
