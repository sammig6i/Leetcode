# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        d = defaultdict(list)
        q = deque([(root, 0)])
        min_col = max_col = 0

        while q:
            node, col = q.popleft()
            if node:
                d[col].append(node.val)

                min_col = min(min_col, col)
                max_col = max(max_col, col)

                q.append((node.left, col - 1))
                q.append((node.right, col + 1))
        return [d[col] for col in range(min_col, max_col + 1)]



        
        

