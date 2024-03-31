from collections import deque

def calculateSpan(arr,n):
    #code here
    result = deque()
    stack = deque()
    for i in range(n):
        while(len(stack) > 0 and arr[stack[-1]] <= arr[i]):
            stack.pop()
        if len(stack) == 0:
            result.append(i+1)
        else:
            result.append(i-stack[-1])
        stack.append(i)
    
    return list(result)

if __name__ == "__main__":
    arr = [6,10,20,15,35,50]
    print(calculateSpan(arr, len(arr)))