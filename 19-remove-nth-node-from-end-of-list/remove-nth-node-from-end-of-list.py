# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right = head
        distance = 0
        while right and distance < n:
            right = right.next
            distance += 1
        
        dummy = ListNode()
        dummy.next = head
        head = dummy
        left = dummy
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next
