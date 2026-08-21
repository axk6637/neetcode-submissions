# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
     
        prev=None
        curr=head

        #1,2,3,4 temp=2 1->None(prev), prev=curr(1), curr=temp(2) 
        #curr=2 temp=3 2->1, prev=2, 
        #curr=3 temp=4 3->2, prev=3
        #curr=4 temp=None 4->3, prev=4

        #4,3,2,1 
        while curr:
            temp=curr.next
            curr.next= prev
            prev=curr
            curr=temp
        return prev





        

