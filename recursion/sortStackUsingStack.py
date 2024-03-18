from collections import deque

# def insert(stack:deque, element:int) -> deque:
#     if len(stack) == 0 or stack[-1] <= element :
#         stack.append(element)
#         return
    
#     last = stack[-1]
#     stack.pop()
#     insert(stack, element)

#     stack.append(last)

# def sortStackHelper(stack: deque, op: deque):
#     if len(stack) == 0:
#         return
#     last = stack[-1]
#     stack.pop()
#     sortStackHelper(stack, op)
#     # Now I have the array arr sorted without last element.
#     # Now I will insert this element into sorted array op.
#     # We use bisect_left for this.
#     # insertion_index = bisect_left(op, last)
#     # op.insert(insertion_index, last)
#     insert(op, element=last)

def insertIntoSortedStack(sortedStack:deque, valueToInsert:int):
    # I check if the stack is empty.
    # I also check if top of sortedStack is smaller than or equal to value to be inserted
    # If yes in either of the cases, I will simply append
    if len(sortedStack) == 0 or sortedStack[-1] <= valueToInsert:
        sortedStack.append(valueToInsert)
        return
    
    topVal = sortedStack.pop()
    insertIntoSortedStack(sortedStack, valueToInsert)
    sortedStack.append(topVal)

def sortStackHelper(stack:deque, op:deque):
    """
    hypothesis is that it'll fill op in ascending order of values from stack

    base condition is that is stack is empty, I simply return, since we don't have to do anything
    """

    if len(stack) == 0:
        return
    
    topOfStack = stack.pop()

    # Now I will first sort the stack without the top. It'll return in op the sorted stack without top of original stack

    sortStackHelper(stack, op)

    # Now inside op, I have to insert topOfStack at the right place
    insertIntoSortedStack(op, topOfStack)




def sortStack(stack : deque) -> deque :
    """
    My hypothesis is that this function takes a list of integers and return the sorted array.
    
    My induction is that if I call it on array without last element, I will get the sorted array without last element.
    Then I will insert the last element into the sorted array using binary search to find the index at which I have to insert.

    My base condition is that is size of array is 1 then simply return, since it's already sorted.
    """
    op = deque()
    sortStackHelper(stack, op)
    return op

if __name__ == "__main__":
    N = deque([2, 3, 7, 6, 4, 5, 9, 8])
    print(sortStack(N))
