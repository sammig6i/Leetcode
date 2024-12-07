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
        res = []
    
        while q:
            temp_map = defaultdict(list)
            for _ in range(len(q)):
                node, col = q.popleft()
                if node:
                    temp_map[col].append(node.val)
                    q.append((node.left, col - 1))
                    q.append((node.right, col + 1))
            for col in temp_map:
                d[col].extend((sorted(temp_map[col])))

        return [d[col] for col in sorted(d)]



    
        

        