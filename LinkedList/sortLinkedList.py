from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def midPoint(self, head:Optional[ListNode]):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def mergeSort(self, head:Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        midPoint = self.midPoint(head)

        left = head
        right = midPoint.next

        midPoint.next = None
        
        leftSorted = self.mergeSort(left)
        rightSorted = self.mergeSort(right)
        dummySorted = ListNode(val=-1)
        t1, t2, t3 = leftSorted, rightSorted, dummySorted
        while t1 and t2:
            if t1.val <= t2.val:
                t3.next = t1
                t1 = t1.next
            else:
                t3.next = t2
                t2 = t2.next
            t3 = t3.next
        while t1:
            t3.next = t1
            t1, t3 = t1.next, t3.next
        while t2:
            t3.next = t2
            t2, t3 = t2.next, t3.next
        return dummySorted.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we will use merge sort
        return self.mergeSort(head)
