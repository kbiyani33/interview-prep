from collections import deque


def recursiveReversal(head, prev):
    if not head:
        return prev
    front = head.next
    head.next = prev
    prev = head
    head = front
    return recursiveReversal(head, prev)

def reverseLinkedList(head):
    if not head or not head.next:
        return head
    return recursiveReversal(head, None)

def reverLLBruteForce(head):
    temp, stack = head, deque()
    while temp:
        stack.append(temp.data)
        temp = temp.next
    temp = head
    while temp:
        temp.data = stack.pop()
        temp = temp.next
    return head

def reverseLinkedList(head):
    prev, t = None, head
    while t:
        front = t.next
        t.next = prev
        prev = t
        t = front
    return prev