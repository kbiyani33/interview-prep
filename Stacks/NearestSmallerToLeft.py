from collections import deque
from typing import List

def nearestSmallerToLeft(arr:List[int], n:int) -> List[int] :
    result = deque()
    stack = deque()

    for i in range(n):
        while len(stack) > 0 and stack[-1] >= arr[i]:
            stack.pop()
        pg = -1 if not stack else stack[-1]
        result.append(pg)
        stack.append(arr[i])

    return result

if __name__ == "__main__":
    arr = [6,10,20,15,35,50]
    print(nearestSmallerToLeft(arr, len(arr)))