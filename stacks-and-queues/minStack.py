from math import inf

class MinStackSpaceNotOptimised:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack or val < self.stack[-1][1]:
            self.stack.append((val, val))
        else:
            minSoFar = self.stack[-1][1]
            self.stack.append((val, minSoFar))

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = inf

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minVal = val
        elif self.minVal <= val:
            self.stack.append(val)
        else:
            self.stack.append(2*val - self.minVal)
            self.minVal = val

    def pop(self) -> None:
        top = self.stack[-1]
        returnVal = -1
        if top < self.minVal:
            returnVal = self.minVal
            self.minVal = 2 * self.minVal - top
        self.stack.pop()
        return returnVal


    def top(self) -> int:
        top = self.stack[-1]
        if top < self.minVal:
            return self.minVal
        else:
            return top

    def getMin(self) -> int:
        return self.minVal


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()