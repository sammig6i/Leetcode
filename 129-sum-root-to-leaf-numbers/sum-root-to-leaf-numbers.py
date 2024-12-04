# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = num = 0

        while root:
            if root.left:
                predecessor = root.left
                steps = 1
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                    steps += 1
                
                if not predecessor.right:
                    num = num * 10 + root.val
                    predecessor.right = root
                    root = root.left
                else:
                    if not predecessor.left:
                        res += num

                    for _ in range(steps):
                        num //= 10
                    predecessor.right = None
                    root = root.right
            else:
                num = num * 10 + root.val
                if not root.right:
                    res += num
                root = root.right
        
        return res
