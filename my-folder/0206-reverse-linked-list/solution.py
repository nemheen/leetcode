# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        if head is None or head.next is None:
            return head

        
        reversed_tail = self.reverseList(head.next)

        # Reverse the pointers
        head.next.next = head
        head.next = None

        # Return the new head of the reversed list
        return reversed_tail
