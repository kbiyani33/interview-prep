class Node:
    def __init__(self, val=0, next=None, child=None):
        self.data = val
        self.next = next
        self.child = child
# Don't change the code above.

def recursive(head):
    if not head.next:
        return head
    nextHead = recursive(head.next)
    t1, t2 = head, nextHead
    t1.next = None
    t2.next = None
    dummy = Node()
    t3 = dummy
    while t1 and t2:
        if t1.data <= t2.data:
            t3.child = t1
            t1 = t1.child
        else:
            t3.child = t2
            t2 = t2.child
        t3 = t3.child
    while t1:
        t3.child = t1
        t1 = t1.child
        t3 = t3.child
    while t2:
        t3.child = t2
        t2 = t2.child
        t3 = t3.child
    return dummy.child

def flattenLinkedList(head: Node) -> Node:
    if not head or not head.next:
        return head
    return recursive(head)