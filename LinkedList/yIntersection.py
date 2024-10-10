from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# brute is obviously with space
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        t1, t2 = headA, headB

        while t1 != t2:
            t1 = t1.next if t1 else headB
            t2 = t2.next if t2 else headA
        
        return t1