# Definition for singly-linked list.


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def bruteForce(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        arr = []
        temp = head
        while temp and temp.next:
            arr.append(temp.val)
            temp = temp.next.next
        if temp: arr.append(temp.val)
        temp = head.next
        while temp and temp.next:
            arr.append(temp.val)
            temp = temp.next.next
        if temp: arr.append(temp.val)

        temp, i = head, 0
        while temp:
            temp.val = arr[i]
            temp = temp.next
            i += 1
        return head
    
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd, even, evenHead = head, head.next, head.next
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = evenHead
        return head
