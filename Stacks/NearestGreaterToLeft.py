from collections import deque
from typing import List

def nearestGreaterToLeft(arr:List[int], n:int) -> List[int] :
    result = deque()
    stack = deque()

    for i in range(n):
        while(len(stack) > 0 and stack[-1] <= arr[i]):
            stack.pop()
        if len(stack) > 0:
            result.append(stack[-1])
        else:
            result.append(-1)
        stack.append(arr[i])
    
    return list(result)

if __name__ == "__main__":
    arr = [6,10,20,15,35,50]
    print(nearestGreaterToLeft(arr, len(arr)))