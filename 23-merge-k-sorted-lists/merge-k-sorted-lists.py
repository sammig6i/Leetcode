# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        return self.divide(lists, 0, len(lists) - 1)
        
    def divide(self, lists, L, R):
        if L > R:
            return None
        if L == R:
            return lists[L]
        
        m = (R + L) // 2
        left = self.divide(lists, L, m)
        right = self.divide(lists, m + 1, R)

        return self.conquer(left, right)
    
    def conquer(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next
