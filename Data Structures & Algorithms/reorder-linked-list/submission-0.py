# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find first and second half

        slow=head
        fast=head.next

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        #reverse second half, save next, reverse, move
        second= slow.next
        prev=None
        slow.next= None
        while second:
            next= second.next
            second.next= prev
            prev=second
            second= next

        #merge both halves
        first=head
        second=prev

        while second:
            tmp1= first.next
            tmp2= second.next
            first.next= second
            second.next= tmp1
            first= tmp1
            second=tmp2



