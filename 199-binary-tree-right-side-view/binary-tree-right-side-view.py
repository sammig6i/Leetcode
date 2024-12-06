# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque([root])
        right_side = []

        while q:
            level = len(q)
            for i in range(level):
                node = q.popleft()
                if node:
                    if i == level - 1:
                        right_side.append(node.val)
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
        return right_side
