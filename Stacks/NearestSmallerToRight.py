from typing import List
from collections import deque

def nearestSmallerToRight(arr:List[int], n:int) -> List[int]:
    result = deque()
    stack = deque()

    for i in range(n-1, -1, -1):
        while(len(stack) > 0 and stack[-1] >= arr[i]):
            stack.pop()
        pg = -1 if len(stack) == 0 else stack[-1]
        result.appendleft(pg)
        stack.append(arr[i])
    
    return list(result)

if __name__ == "__main__":
    arr = [6,10,20,15,35,50]
    print(nearestSmallerToRight(arr, len(arr)))