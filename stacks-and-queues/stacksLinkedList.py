class Node:
    def __init__(self, data:int) -> None:
        self.data = data
        self.next = None

class StackUsingLL:
    
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, x:int):
        node = Node(data=x)
        node.next = self.top
        self.top = node
        self.size += 1
    
    def peek(self) -> int:
        if not self.top:
            raise Exception("cannot peek in empty stack")
        return self.top.data
    
    def pop(self) -> int:
        if not self.top:
            raise Exception("cannot pop from empty stack")
        node = self.top
        self.top = node.next
        self.size -= 1
        return node.data
    
    