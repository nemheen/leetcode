# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ca, cb = headA, headB
        lena, lenb = 0, 0
        lasta, lastb = headA, headB
        if not headA or not headB:
            return None

        while lasta.next:
            lasta = lasta.next
            lena = lena + 1
        while lastb.next:
            lastb = lastb.next
            lenb = lenb + 1
        if lasta!=lastb:
            return None
        if lena > lenb:
            while lena > lenb:
                ca = ca.next
                lena -= 1
        if lenb > lena:
            while lenb > lena:
                cb = cb.next
                lenb -= 1
        while ca != cb:
            ca = ca.next
            cb = cb.next
        return ca

