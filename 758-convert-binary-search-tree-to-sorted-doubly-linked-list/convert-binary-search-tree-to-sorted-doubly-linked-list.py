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
        first = last = None
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            node = stack.pop()
            if not first:
                first = node
            
            if last:
                last.right = node
                node.left = last
            last = node

            cur = node.right
            
        first.left = last
        last.right = first
        return first