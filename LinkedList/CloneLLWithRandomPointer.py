"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from typing import Optional
class Solution:
    def copyRandomListONSpace(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # This is returning the node using O(N) space and O(N) time
        if not head:
            return None
        hashTable = {}
        temp = head

        while temp:
            node = Node(x = temp.val)
            hashTable[temp] = node
            temp = temp.next
        
        X = head
        while X:
            hashTable[X].next = hashTable[X.next] if X.next else None
            hashTable[X].random = hashTable[X.random] if X.random else None
            X = X.next
            
        
        return hashTable[head]
    
    def copyRandomListO1Space(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # This is returning the node using O(N) space and O(N) time
        if not head:
            return None
        
        temp = head
        while temp:
            node = Node(x=temp.val)
            next = temp.next
            temp.next = node
            node.next = next
        
        X = head
        while X and X.next:
            # I need the next and random to be fixed
            X.next.next = X.next.next.next if X.next.next else None
            X.next.random = X.random.next if X.random else None
            X = X.next.next
        
        return head.next

            

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        return self.copyRandomListONSpace(head)
        