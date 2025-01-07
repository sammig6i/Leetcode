# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        d = 2
        while prev.next:
            node = prev
            n = 0
            for _ in range(d):
                if not node.next:
                    break
                n += 1
                node = node.next
            if n & 1:
                prev = node
            else:
                group_start = prev.next
                node = prev.next
                rev = None
                for _ in range(n):
                    next_node = node.next
                    node.next = rev
                    node, rev = next_node, node
                
                next_prev = prev.next
                group_start.next = node
                prev.next = rev
                prev = next_prev
            d += 1
        return head