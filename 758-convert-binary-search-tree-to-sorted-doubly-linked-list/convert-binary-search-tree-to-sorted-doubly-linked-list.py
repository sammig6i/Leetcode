"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        first = last = None

        def dfs(node):
            nonlocal first, last
            if not node:
                return None
            
            dfs(node.left)

            if not last:
                first = node
            else:
                last.right = node
                node.left = last
            
            last = node

            dfs(node.right)

        
        dfs(root)

        first.left = last
        last.right = first
        return first
