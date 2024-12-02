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
        curr = root
        head = prev = None

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            node = stack.pop()
            node.left = prev
            if prev:
                prev.right = node
            prev = node

            if not head:
                head = node
            
            curr = node.right
        
        head.left = prev
        prev.right = head

        return head