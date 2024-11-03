from stacksLinkedList import Node

class QueueLL:
    def __init__(self) -> None:
        self.start, self.end = None, None
        self.size = 0
    
    def push(self, x:int) -> None:
        node = Node(data=x)
        if not self.start and not self.end:
            self.start = node
            self.end = node
        else:
            self.end.next = node
            self.end = self.end.next
        self.size += 1
    
    def peek(self) -> int:
        if not self.start:
            raise Exception("cannot peek in empty queue")
        return self.start.data
    
    def pop(self) -> int:
        if not self.start and not self.end and self.size == 0:
            raise Exception("cannot pop from empty queue")
        
        popNode = self.start
        self.start = popNode.next
        self.size -= 1
        if self.size == 0:
            self.start, self.end = None, None
        return popNode.data
        
