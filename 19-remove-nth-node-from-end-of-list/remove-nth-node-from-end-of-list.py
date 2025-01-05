# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        while cur:
            size += 1
            cur = cur.next
        
        nth_node = size - n + 1
        cycle = 0
        cur = head
        prev = dummy
        while cur:
            cycle += 1
            if cycle == nth_node:
                prev.next = cur.next
                break
            prev, cur = cur, cur.next
        return dummy.next


        

