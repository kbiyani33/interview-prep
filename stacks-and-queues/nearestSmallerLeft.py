# cook your dish here
from typing import List

def previousSmallerElement(n:int, arr:List[int]) -> List[int]:
    result = [-1 for _ in range(n)]
    stack = [arr[0]]
    
    for i in range(1, n):
        topOfStack = stack[-1]
        if topOfStack < arr[i]:
            result[i] = topOfStack
        else:
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            if stack:
                result[i] = stack[-1]
        stack.append(arr[i])
    
    return result
    


if __name__ == "__main__":
    t = int(input())
    while t:
        n = int(input())
        arr = [int(i) for i in input().strip().split(" ")]
        res = previousSmallerElement(n=n, arr=arr)
        for i in res:
            print(i, end=" ")
        print()
        t -= 1
        