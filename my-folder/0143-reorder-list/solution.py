class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def findMiddle(node):
            slow = fast = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverseList(node):
            prev = None
            curr = node
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        def mergeTwoLists(list1, list2):
            while list2:
                temp1, temp2 = list1.next, list2.next
                list1.next, list2.next = list2, temp1
                list1, list2 = temp1, temp2

        if not head or not head.next:
            return

        
        middle = findMiddle(head)

        reversed_second_half = reverseList(middle.next)
        middle.next = None  
        mergeTwoLists(head, reversed_second_half)

