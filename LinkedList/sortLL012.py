'''
Following is the structure of the Node class already defined.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def sortList(head):
    if not head or not head.next:
        return head

    zeroHead, oneHead, twoHead = Node(-1), Node(-1), Node(-1)
    zero, one, two = zeroHead, oneHead, twoHead
    temp = head
    while temp:
        if temp.data==0:
            zero.next = temp
            zero = zero.next
        elif temp.data==1:
            one.next=temp
            one = one.next
        else:
            two.next=temp
            two = two.next
        temp = temp.next
    
    if oneHead:
        zero.next = oneHead.next
    else:
        zero.next = twoHead.next
    
    if twoHead:
        one.next = twoHead.next
    else:
        oneHead.next = None

    two.next = None
    
    return zeroHead.next

def sortList(head):
    # Write your code here
    temp = head
    c0, c1, c2 = 0, 0, 0
    while temp:
        if temp.data==0: c0 += 1
        elif temp.data==1: c1 += 1
        else: c2 += 1
        temp = temp.next
    temp = head
    for i in range(c0):
        temp.data = 0
        temp = temp.next

    for i in range(c1):
        temp.data = 1
        temp = temp.next

    for i in range(c2):
        temp.data = 2
        temp = temp.next
    
    return head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def sortList(head):
    if not head or not head.next:
        return head
    
    zeroDummy = Node(data=0)
    zeroTemp = zeroDummy

    oneDummy = Node(data=1)
    oneTemp = oneDummy

    twoDummy = Node(data=2)
    twoTemp = twoDummy

    temp = head
    while temp:
        if temp.data == 0:
            zeroTemp.next = temp
            zeroTemp = zeroTemp.next
        elif temp.data == 1:
            oneTemp.next = temp
            oneTemp = oneTemp.next
        else:
            twoTemp.next = temp
            twoTemp = twoTemp.next
        temp = temp.next
    
    """
    Case 1 -> 0 exists
        1.a -> 1 exists
        1.b -> 1 doesn't exist and 2 exists
    """ 
    oneTemp.next = twoDummy.next
    twoTemp.next = None
    zeroTemp.next = oneDummy.next
    return zeroDummy.next if zeroDummy.next else oneDummy.next if oneDummy.next else twoDummy.next