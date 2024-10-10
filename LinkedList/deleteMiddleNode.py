# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevOfMiddle = ListNode(-1) # dummy node for prevOfMiddleious
        prevOfMiddle.next = head
        slow, fast = head, head
        while fast and fast.next:
            prevOfMiddle = prevOfMiddle.next
            fast = fast.next.next
        return prevOfMiddle
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return None

        prevOfMiddle = self.getMiddle(head)
        prevOfMiddle.next = prevOfMiddle.next.next
        return head

