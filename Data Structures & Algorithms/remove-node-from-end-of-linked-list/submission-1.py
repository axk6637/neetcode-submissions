# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """dummy=ListNode(0)
        dummy.next=head

        slow=dummy
        fast=dummy 

        for node in range(n + 1):
            fast = fast.next
        # Move both pointers until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next
        # Now slow is just before the node to remove
        slow.next = slow.next.next
        # Return the new head of the list
        return dummy.next
        """
        dummy= ListNode()
        dummy.next=head
        left= dummy
        right= head
        while n>0 and right:
            right= right.next
            n-=1
        while right:
            left=left.next
            right=right.next

        #delete
        left.next=left.next.next

        return dummy.next
