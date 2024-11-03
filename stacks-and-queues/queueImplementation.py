class QueueImplementation:
    def __init__(self, capacity:int=100):
        self.capacity = capacity
        self.queue = [None for _ in range(capacity)]
        self.start, self.end = -1, -1
        self.cursize = 0
    
    def push(self, x:int) -> None:
        if self.cursize == self.capacity:
            raise Exception("cannot add more elements since queue is already full")
        if self.start == -1 and self.end == -1 and self.cursize == 0:
            self.start += 1
        self.end = (self.end + 1) % self.capacity
        self.cursize += 1
        self.queue[self.end] = x
    
    def top(self) -> int:
        if self.cursize == 0:
            raise Exception("peeking from an empty queue :)")
        
        return self.queue[self.start]
    
    def pop(self) -> int:
        # if empty then no point
        if self.cursize == 0:
            raise Exception("popping from empty queue :(")
        
        val = self.queue[self.start]
        self.start = (self.start + 1) % self.capacity
        self.cursize -= 1
        if self.cursize == 0:
            self.start = -1
            self.end = -1
        return val
        

        