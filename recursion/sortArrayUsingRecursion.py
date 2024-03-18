from typing import List
from bisect import bisect_left

def insert(arr:List[int], element:int) -> List[int]:
    if len(arr) == 0 or arr[-1] <= element :
        arr.append(element)
        return
    
    last = arr[-1]
    arr.pop()
    insert(arr, element)

    arr.append(last)

def sortArrayHelper(arr: List[int], op: List[int]):
    if len(arr) == 0:
        return
    last = arr[-1]
    sortArrayHelper(arr[:-1], op)
    # Now I have the array arr sorted without last element.
    # Now I will insert this element into sorted array op.
    # We use bisect_left for this.
    # insertion_index = bisect_left(op, last)
    # op.insert(insertion_index, last)
    insert(op, element=last)


def sortArray(arr : List[int]) -> List[int] :
    """
    My hypothesis is that this function takes a list of integers and return the sorted array.
    
    My induction is that if I call it on array without last element, I will get the sorted array without last element.
    Then I will insert the last element into the sorted array using binary search to find the index at which I have to insert.

    My base condition is that is size of array is 1 then simply return, since it's already sorted.
    """
    op = []
    sortArrayHelper(arr, op)
    return op

if __name__ == "__main__":
    N = [2, 3, 7, 6, 4, 5, 9]
    print(sortArray(N))
