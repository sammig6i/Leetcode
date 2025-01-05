# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        cur = slow
        while cur:
            next_node = cur.next
            cur.next = prev
            prev, cur = cur, next_node
        
        cur = head
        first = prev
        while cur and first:
            if cur.val != first.val:
                return False
            cur = cur.next
            first = first.next
        return True
        

        

