# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        left = dummy
        count = k
        while count > 0:
            count -= 1
            left = left.next
        
        N = 0
        cur = head
        while cur:
            N += 1
            cur = cur.next

        right_idx = N - k
        right = head
        for i in range(N):
            if i == right_idx:
                break
            right = right.next
        
        left.val, right.val = right.val, left.val
        return dummy.next

        

        
