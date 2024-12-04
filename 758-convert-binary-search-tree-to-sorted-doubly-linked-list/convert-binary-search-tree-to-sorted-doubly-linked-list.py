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
        
        stack = []
        cur = root
        first = last = None

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            node = stack.pop()
            node.left = last
            if last:
                last.right = node
            last = node

            if not first:
                first = node
            
            cur = node.right
        
        first.left = last
        last.right = first

        return first