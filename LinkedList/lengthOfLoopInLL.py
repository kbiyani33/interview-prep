# Node is defined as :
class Node:
   def __init__(self, val=0):
       self.val = val
       self.next = None
 
def bruteForce(head):
    #Return -1 if no loop exists else return the size of the loop
    nodemap = {}
    temp, timer = head, 1
    while temp:
        if temp in nodemap:
            return timer - nodemap.get(temp)
        nodemap[temp] = timer
        timer += 1
        temp = temp.next
    return -1
 
def findLength(slow:Node, fast:Node):
    counter = 1
    fast = fast.next
    while slow != fast:
        fast = fast.next
        counter += 1
    return counter

def Optimal(head):
    #Return -1 if no loop exists else return the size of the loop
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # this means the loop is detected
            return findLength(slow, fast)
    
    return -1