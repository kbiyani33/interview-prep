from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Brute force is obviously count number of nodes in 1 pass
# remove L-N+1th node and hoorayy
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return head
        if not head.next: return None
        slow = ListNode(val=-1)
        slow.next = head # attaching dummy pointer

        fast = head
        for i in range(n):
            fast = fast.next
        if not fast: # nth node from end is head, remove head
            return head.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head