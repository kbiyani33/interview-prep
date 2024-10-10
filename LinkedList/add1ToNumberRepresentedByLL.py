class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Don't change the code above.

def reverse(head:Node) -> Node:
    if not head or not head.next:
        return head
    
    prev = None
    temp = head
    
    while temp:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    
    return prev

def addOne(head: Node) -> Node:
    if not head: return None

    headReverse = reverse(head)

    t1 = headReverse
    carry = 1
    dummy = Node(-1)
    t3 = dummy
    while t1 or carry:
        val = carry
        if t1: 
            val += t1.data
            t1 = t1.next
        t3.next = Node(data=val%10)
        carry = val // 10
        t3 = t3.next
    final = dummy.next
    return reverse(final)

def recursiveBacktrackingSoln(head: Node, carry) -> Node:
    if not head:
        return None

    recursiveBacktrackingSoln(head.next, carry)

    # I'll now add the carry to this node's value
    totalVal = head.data + carry[0]
    head.data = totalVal % 10
    carry[0] = totalVal//10
    return head

def addOne(head: Node) -> Node:
    carry = [1]
    temp = head
    recursiveBacktrackingSoln(temp, carry)
    if carry[0] > 0 :
        newNode = Node(data=carry[0])
        newNode.next = head
        head = newNode
    return head