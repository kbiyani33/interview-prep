from collections import deque

"""
Middle element to be deleted = (size of stack)/2 + 1

I have to delete this element.

HYPOTHESIS -
My deleteNthElementOfStack will delete nth element and return the stack again.

If i can remove nth element from stack, I can remove the n-1th element from stack without the top

INDUCTION -
I simply push the removed top of stack into the stack from with middle(nth element) element is removed.

BASE CONDITION -
if input n is 1, then simply return after popping the top.
"""

def deleteNthElementOfStack(stack:deque, N:int):
    if N == 1:
        stack.pop()
        return
    top = stack[-1]
    stack.pop()
    deleteNthElementOfStack(stack, N-1)
    stack.append(top)
    

if __name__ == "__main__":
    N = deque([2, 3, 7, 6, 4, 5, 9])
    middle = len(N)/2 + 1
    deleteNthElementOfStack(N, middle)
    print(N)