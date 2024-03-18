from typing import List
from bisect import bisect_left

# def insertIntoSortedArray(arr: List[int], op:List[int], element: int):
#     """
#     Hypothesis --> 
#     arr is sorted, so if I insert <element> into array, arr is still sorted.

#     Base Condition --> 
#     If my arr is empty, I simply insert the element and return

#     Induction --> 
#     if I insert element into arr, it'll remain sorted. 
#     So if I insert element into arr without last element, it'll also remain sorted.
#     Now my array is already sorted, so, last element is always the largest one.
#     So I will insert it into that position, where last element is smaller than or equal to element to be inserted.
#     Basically if arr = [1, 3, 5]
#     I want to insert 2
#     is 2 >= 5 ? NO
#         so remove 5 and call  insert([1, 3], 2)
#         is 2 >= 3 ? NO
#             so remove 3 and call  insert([1], 2)
#             Is 2 >= 1 ? YES
#                 so append 2
#                 return
#             append 3
#             return
#         append 5
#         return 
#     Finally we get [1, 2, 3, 5]
#     """
#     if len(arr) == 0 or element >= arr[-1]:
#         op += arr + [element]
#         return
    
#     last = arr[-1]
#     insertIntoSortedArray(arr=arr[:-1],op=op, element=element)
#     op.append(last)

def insert(arr:List[int], element:int) -> List[int]:
    if len(arr) == 0 or arr[-1] <= element :
        arr.append(element)
        return
    
    last = arr[-1]
    arr.pop()
    insert(arr, element)

    arr.append(last)

if __name__ == "__main__":
    N = [1, 3, 5]
    insert(N, 2)
    print(N)
