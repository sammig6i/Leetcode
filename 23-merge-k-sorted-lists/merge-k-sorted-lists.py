# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        head = ListNode()
        tail = head

        while True:
            min_node = -1
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if min_node == -1 or lists[min_node].val > lists[i].val:
                    min_node = i
            
            if min_node == -1:
                break
            tail.next = lists[min_node]
            tail = tail.next
            lists[min_node] = lists[min_node].next

        return head.next



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
