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
        
        def dfs(node):
            nonlocal first, last
            if not node:
                return None
            
            dfs(node.left)

            if not last:
                first = node
            else:
                node.left = last
                last.right = node
    
            last = node

            dfs(node.right)

        first, last = None, None

        dfs(root)

        first.left = last
        last.right = first

        return first


            
            
