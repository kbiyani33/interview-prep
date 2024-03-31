"""
This question is also known as nearest greater to right

The Next greater Element for an element x is the first greater element on the right side of x in the array. 

Elements for which no greater element exist, consider the next greater element as -1. 

Example: 

Input: arr[] = [ 4 , 5 , 2 , 25 ]
Output: 4      >   5
        5      >   25
        2      >   25
        25     >   -1
Explanation: except 25 every element has an element greater than them present on the right side

Input: arr[] = [ 13 , 7, 6 , 12 ]
Output: 13      >    -1
        7       >     12
        6       >     12
        12      >     -1
Explanation: 13 and 12 dont have any element greater than them present on the right side
"""

from collections import deque
def nextLargerElement(arr,n):
    #code here
    stack = deque()
    result = deque()
    for i in range(n-1, -1, -1):
        while len(stack) > 0 and stack[-1] <= arr[i]:
            stack.pop()
        if len(stack) > 0:
            result.appendleft(stack[-1])
        else:
            result.appendleft(-1)
        stack.append(arr[i])
    
    return list(result)