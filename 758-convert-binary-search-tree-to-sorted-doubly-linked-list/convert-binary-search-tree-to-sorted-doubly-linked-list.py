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
        self.first = self.last = None

        self.dfs(root)

        self.first.left = self.last
        self.last.right = self.first
        return self.first
    
    def dfs(self, node):
        if not node:
            return None
        
        self.dfs(node.left)

        if not self.first:
            self.first = node
        else:
            self.last.right = node
            node.left = self.last
        
        self.last = node
        self.dfs(node.right)