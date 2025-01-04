# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    
        if left == 1:
            new_head, _ = self.reverseList(head, right)
            return new_head
        
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head
    
    def reverseList(self, node, n):
        if n == 1:
            return node, node.next
        new_head, next_node = self.reverseList(node.next, n - 1)
        node.next.next = node
        node.next = next_node
        return new_head, next_node