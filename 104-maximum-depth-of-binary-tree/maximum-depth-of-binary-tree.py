# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 0]]
        max_depth = 0
        if not root:
            return 0
        
        while stack:
            for i in range(len(stack)):
                node, depth = stack.pop()
                max_depth = max(depth, max_depth)
                if node:
                    stack.append([node.right, depth + 1])
                    stack.append([node.left, depth + 1])

        return max_depth


        
        


       

        
        
        