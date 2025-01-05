# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        sublist_head = head
        for _ in range(left - 1):
            prev = prev.next

        sublist_head = prev.next
        sublist_tail = sublist_head
        for _ in range(right - left):
            sublist_tail = sublist_tail.next
        
        next_node = sublist_tail.next
        sublist_tail.next = None
        reversed_list = self.reverseList(sublist_head)
        prev.next = reversed_list
        sublist_head.next = next_node

        return dummy.next
    
    def reverseList(self, head):
        if not head: return None

        prev = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev, cur = cur, next_node
        return prev
