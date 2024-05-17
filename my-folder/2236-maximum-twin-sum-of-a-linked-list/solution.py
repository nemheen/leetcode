# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return None

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        def reverse(head):
            prev = None
            curr = head

            while curr:
                forw = curr.next
                curr.next = prev
                prev = curr
                curr = forw
            return prev
        
        sec = reverse(slow)

        most = 0
        first = head

        while sec:
            most = max(most, first.val+sec.val)
            first = first.next
            sec = sec.next

        return most
