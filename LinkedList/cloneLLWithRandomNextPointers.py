"""
# Definition for a Node.
"""

from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        if not head.next:
            node = Node(head.val)
            if head.random: # then it means it can only point to itself
                node.random = node
            return node
        
        # step 1 -> copy each node
        temp = head
        while temp:
            node = Node(temp.val, next=temp.next)
            temp.next = node
            temp = temp.next.next
        
        # step 2 -> copy the random pointers
        temp = head
        while temp:
            random = temp.random
            # random can be another node or null
            if random:
                temp.next.random = random.next
            temp = temp.next.next
        
        # step 3 -> copy the next nodes
        temp = head.next
        while temp and temp.next:
            nextTemp = temp.next.next
            temp.next = temp.next.next
            temp = nextTemp
        return head.next
            