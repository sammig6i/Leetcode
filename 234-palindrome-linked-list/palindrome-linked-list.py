# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev, slow = slow, next_node
        
        cur = head
        while cur and prev:
            if cur.val != prev.val:
                return False
            cur = cur.next
            prev = prev.next
        return True
            