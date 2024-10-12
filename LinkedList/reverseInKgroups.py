# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseLL(self, head: Optional[ListNode]):
        if not head or not head.next: 
            return head

        prev, temp = None, head
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev

    def findKthNode(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp, count = head, 1
        while temp:
            if count == k:
                return temp
            temp = temp.next
            count += 1
        return None
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 1:  # No need to change if k==1
            return head

        dummy = ListNode(0)
        dummy.next = head
        prevGroupEnd = dummy
        temp = head

        while temp:
            kthNode = self.findKthNode(temp, k)
            if not kthNode:
                break

            nextGroupStart = kthNode.next
            kthNode.next = None  # Temporarily end the current segment

            # Reverse the current segment
            reversedHead = self.reverseLL(temp)

            # Connect the previous segment to the reversed segment
            prevGroupEnd.next = reversedHead

            # Connect the reversed segment to the next segment
            temp.next = nextGroupStart

            # Update prevGroupEnd and temp for the next iteration
            prevGroupEnd = temp
            temp = nextGroupStart

        return dummy.next
