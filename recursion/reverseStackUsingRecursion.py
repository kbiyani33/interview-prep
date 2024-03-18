from collections import deque

def insert_at_bottom(stack:deque, element:int, n:int):
    if n==0:
        stack.append(element)
        return
    
    val = stack.pop()
    insert_at_bottom(stack, element, n-1)
    stack.append(val)
    

def reverse_stack(stack:deque, n:int):
    """
    HYPOTHESIS is that rever_stack will return a stack in reversed order.

    BASE CONDITION is that if the length of stack is 1, then simply return. Since it can be left as it is.

    INDUCTION is that I need to take the top value and that will be inserted to the end of the array
    """

    if n==1: # n = length of the stack in question basically.
        return
    
    topOfStack = stack.pop()
    reverse_stack(stack, n-1)
    # Now i have to insert the top i took out at the bottom of the stack. For this I'll write one more recursive function.
    insert_at_bottom(stack, topOfStack, n-1)
    

if __name__ == "__main__":
    stack = deque([1, 3, 5, 2342, 34,5, 34, 63,4])
    n = len(stack)
    reverse_stack(stack, n)
    print(stack)