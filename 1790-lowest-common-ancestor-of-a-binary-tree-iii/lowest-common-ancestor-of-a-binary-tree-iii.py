"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_depth = self.get_depth(p, 0)
        q_depth = self.get_depth(q, 0)

        for _ in range(p_depth - q_depth):
            p = p.parent
        for _ in range(q_depth - p_depth):
            q = q.parent
        
        while p != q:
            p = p.parent
            q = q.parent
        return p
    
    def get_depth(self, node, depth):
        while node:
            depth += 1
            node = node.parent
        return depth