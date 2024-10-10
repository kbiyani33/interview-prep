from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head

        count = 1
        tail = head
        while tail.next:
            tail = tail.next
            count += 1
        
        if k%count == 0: return head
        k = k%count
        
        # step 1 is to make the next of tail to become the original head
        tail.next = head
        # step 2 is to make the traversal of N-k nodes from original head
        temp = head
        i = 1
        while i < count-k:
            temp = temp.next
            i += 1
        # newHead = next of temp
        newHead = temp.next
        temp.next = None
        return newHead