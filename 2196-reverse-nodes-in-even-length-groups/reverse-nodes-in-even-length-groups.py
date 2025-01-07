class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head: ListNode, k: int) -> ListNode:
            """Helper function to reverse the first k nodes of a linked list."""
            prev, curr = None, head
            for _ in range(k):
                if not curr:
                    break
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        def helper(head: ListNode, group_size: int) -> ListNode:
            """Recursive function to process groups."""
            # Base case: if there are no more nodes, return
            if not head:
                return None

            # Traverse to find the group size
            node = head
            count = 0
            while node and count < group_size:
                count += 1
                node = node.next

            # If group length is even, reverse it
            if count % 2 == 0:
                reversed_head = reverse(head, count)
                head.next = helper(node, group_size + 1)
                return reversed_head
            else:
                # Otherwise, keep it as is and process the next group
                node = head
                for _ in range(count - 1):
                    node = node.next
                node.next = helper(node.next, group_size + 1)
                return head

        return helper(head, 1)
