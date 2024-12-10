"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        node = Node(insertVal)

        if not head:
            head = node
            head.next = head
            return head
        
        prev, cur = head, head.next

        while cur != head:
            # 1 -> Node(2) -> 3
            if prev.val <= node.val <= cur.val:
               break

            # 4 -> Node(5) -> 1, 4 -> Node(0) -> 1
            elif prev.val > cur.val and (node.val > prev.val or node.val < cur.val):
                break

            prev, cur = cur, cur.next
        

        node.next = cur
        prev.next = node

        return head
        # 3, 4, 0, 1