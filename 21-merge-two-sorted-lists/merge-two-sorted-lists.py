# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = head = ListNode(0)
        l1 = list1
        l2 = list2

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1, curr = l1.next, l1
            else:
                curr.next = l2
                l2, curr = l2.next, l2
        
        if l1 or l2:
            curr.next = l1 if l1 else l2
        
        return head.next

