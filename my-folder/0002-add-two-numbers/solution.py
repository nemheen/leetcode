# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        out = []
        temp, carry = 0, 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            temp = v1 + v2 + carry
            carry = temp // 10
            out.append(temp%10)
            if l1: l1 = l1.next
            if l2: l2 = l2.next
     
        if carry > 0:
            out.append(carry)
        res = ListNode(0)
        curr = res
        for o in out:
            curr.next = ListNode(o)
            curr = curr.next
        return res.next




