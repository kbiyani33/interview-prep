"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr, carry, t1, t2 = dummy, 0, l1, l2
        while t1 or t2:
            currNodeVal = carry
            if t1: 
                currNodeVal += t1.val
                t1 = t1.next
            if t2: 
                currNodeVal += t2.val
                t2 = t2.next
            
            carry = currNodeVal//10
            finalValuePicked = currNodeVal % 10
            curr.next = ListNode(finalValuePicked)
            curr = curr.next
        
        if carry != 0: curr.next = ListNode(val=carry)
        return dummy.next