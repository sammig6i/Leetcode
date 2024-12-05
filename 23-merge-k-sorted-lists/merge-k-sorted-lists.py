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
        cur = head

        while True:
            min_node = -1

            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if min_node == -1 or lists[min_node].val > lists[i].val:
                    min_node = i

            if min_node == -1:
                break
            else:
                cur.next = lists[min_node]
                lists[min_node] = lists[min_node].next
                cur = cur.next
        return head.next