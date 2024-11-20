# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return None
            if len(res) == depth:
                res.append(node.val)
            else:
                res[depth] = max(res[depth], node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return res




        # q = deque([root])
        # res = []
        # if not root:
        #     return []

        # while q:
        #     max_node = float("-inf")
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node:
        #             max_node = max(max_node, node.val)
        #             if node.left: q.append(node.left)
        #             if node.right: q.append(node.right)
        #     res.append(max_node)
        # return res