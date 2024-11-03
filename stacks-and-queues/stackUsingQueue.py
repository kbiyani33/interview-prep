from collections import deque
class Stack:

    def __init__(self):
        self.q = deque()
    
    def push(self, x:int) -> None:
        q = self.q
        size = len(q)
        q.append(x)
        for _ in range(size):
            val = q.popleft()
            q.append(val)
    
    def top(self) -> int:
        if not self.q:
            raise Exception("cannot peek in empty queue")
        return self.q[0]
    
    def pop(self) -> int:
        if not self.q:
            raise Exception("cannot pop in empty queue")
        return self.q.popleft()


    