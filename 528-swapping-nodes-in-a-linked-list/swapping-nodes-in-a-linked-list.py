# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = head
        fast = head
        for _ in range(k - 1):
            fast = fast.next
        first = fast

        while fast.next:
            fast = fast.next
            slow = slow.next
        first.val, slow.val = slow.val, first.val
        return head