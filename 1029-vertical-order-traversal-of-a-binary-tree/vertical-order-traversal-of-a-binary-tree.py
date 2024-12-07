# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        
        d = defaultdict(list)
        q = deque([(root, 0)])

        while q:
            d1 = defaultdict(list)
            for _ in range(len(q)):
                node, col = q.popleft()
                if node:
                    d1[col].append(node.val)
                    q.append((node.left, col - 1))
                    q.append((node.right, col + 1))
            for key in d1:
                d[key] += (sorted(d1[key]))

        return [d[key] for key in sorted(d)]



    
        

        