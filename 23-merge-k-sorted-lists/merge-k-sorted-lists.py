# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        nodes = []
        for lst in lists:
            while lst:
                nodes.append(lst.val)
                lst = lst.next
        nodes.sort()

        head = ListNode()
        cur = head
        for node in nodes:
            cur.next = ListNode(node)
            cur = cur.next
        return head.next
        
        
        
        


        
    
    
