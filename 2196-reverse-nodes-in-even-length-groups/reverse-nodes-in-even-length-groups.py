# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = 2
        prev = head
        while prev.next:
            node = prev
            n = 0
            for _ in range(d):
                if not node.next:
                    break
                node = node.next
                n += 1
            
            if n & 1:
                prev = node
            else:
                group_start = prev.next
                cur = prev.next
                rev = None
                for _ in range(n):
                    next_node = cur.next
                    cur.next = rev
                    rev, cur = cur, next_node
                next_prev = prev.next
                group_start.next = cur
                prev.next = rev
                prev = next_prev
            d += 1
        return head