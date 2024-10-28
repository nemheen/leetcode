# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h1 = odd = ListNode()
        h2 = even = ListNode()

        h = head
        i = 0
        while h:
            if i%2==0:
                even.next = h
                even = even.next

            else:
                odd.next = h
                odd = odd.next
            h = h.next
            i += 1
        odd.next = None
        even.next = h1.next
        return h2.next

        
