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
        
        q = deque([root, 0])
        res = []
        cur = root
        while q: 
            prev, cur = cur, q.popleft()
            while cur:
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
                prev, cur = cur, q.popleft()
            res.append(prev.val)
            if q:
                q.append(None)
        return res