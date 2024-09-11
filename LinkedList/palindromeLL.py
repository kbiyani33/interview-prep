# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseLL(self, head):
        temp, prev = head, None
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Now slow is in mid point
        # Fast is in the end.
        # We will reverse the linked list from next of slow and compare
        
        reverse2ndHalf = self.reverseLL(slow.next)
        slow.next = None
        t1, t2 = head, reverse2ndHalf
        while t1 and t2:
            if t1.val != t2.val:
                return False
            t1 = t1.next
            t2 = t2.next
        return True
