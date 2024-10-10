'''
Following is the structure of the Node class already defined.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def SpaceTakingSolution(head):
    nodeMap = {}
    temp = head
    while temp:
        if temp in nodeMap:
            return temp
        nodeMap[temp] = temp.data
        temp = temp.next
    return None

def OptimalCode(head):
    # Write your code here
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow==fast:
            # loop detected
            slow = head
            while slow!=fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None