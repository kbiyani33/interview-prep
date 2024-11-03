class Queue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def push(self, x:int) -> None:
        s1, s2 = self.s1, self.s2
        for _ in range(len(s1)):
            s2.append(s1.pop())
        s1.append(x)
        for _ in range(len(s2)):
            s1.append(s2.pop())
        return
    
    def top(self) -> int:
        if not self.s1:
            raise Exception("cannot peek in empty stack")
        return self.s1[-1]
    
    def pop(self) -> int:
        if not self.s1:
            raise Exception("cannot pop from empty stack")
        return self.s1.pop()


class Queue2:

    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def push(self, x:int) -> None:
        self.s1.append(x)
    
    def pop(self) -> int:
        s1, s2 = self.s1, self.s2
        if s2:
            return s2.pop()
        if not s1:
            raise Exception("cannot pop from empty q")
        for _ in range(len(s1)):
            s2.append(s1.pop())

        return s2.pop()
    
    def top(self) -> int:
        s1, s2 = self.s1, self.s2
        if s2:
            return s2[-1]
        if not s1:
            raise Exception("cannot peek from empty q")
        for _ in range(len(s1)):
            s2.append(s1.pop())
        return s2[-1]

q = Queue2()
q.push(4)
q.push(2)
q.push(3)
print(q.top())  # Output: 4
print(q.pop())  # Output: 4
print(q.pop())  # Output: 2