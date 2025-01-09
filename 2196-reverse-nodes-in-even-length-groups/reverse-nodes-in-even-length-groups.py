class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to reverse a linked list
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
    
    def reverseEvenLengthGroups(self, head: ListNode) -> ListNode:
        # Creating a dummy node to avoid adding checks for the first node
        dummy = ListNode()
        dummy.next = head
        
        prev = dummy
        # Loop to determine the lengths of groups
        length = 1
        while head:
            tail = head
            next_head = None
            
            # Determining the length of the current group
            j = 1
            while j < length and tail and tail.next:
                tail = tail.next
                j += 1
            
            # Head of the next group
            next_head = tail.next
            
            if j % 2 == 0:
                # If even-sized group is found
                # Reversing the group and setting prev and head appropriately
                tail.next = None
                prev.next = self.reverseList(head)
                prev = head
                head.next = next_head
                head = next_head
            else:
                # If group is odd-sized, simply move to the next group
                prev = tail
                head = next_head
            
            # Increase the group size
            length += 1
        
        # Returning the head of the modified list
        return dummy.next
