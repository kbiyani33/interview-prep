from typing import List
from bisect import bisect_left, bisect_right

def binary_search_ascending(arr: List[int], N:int, query:int) -> int:
    start = 0
    end = N-1
    while(start <= end):
        middle = start + (end-start)//2 # we do this to prevent integer overflow. Not needed in python but good to know.
        if arr[middle] == query:
            return middle
        if query > arr[middle]: # this means that the element is in the right side of the array
            start = middle + 1
        else:
            end = middle - 1
    return -1

def binary_search_descending(arr:List[int], N:int, query:int) -> int:
    start, end = 0, N-1

    while(start <= end):
        middle = start + (end-start)//2 # not needed in python but in other programming languages is needed for avoiding overflow

        if arr[middle] == query:
            return middle
        
        if query > arr[middle] : # In this case it'll be on left side since it's descending
            end = middle - 1
        else:
            start = middle + 1
    
    return -1


if __name__=="__main__":
    arr = [2, 4, 5, 6, 8, 11, 32, 43]
    arrDes = [43, 32, 11, 8, 6, 5, 4, 2]
    query = 11

    print(binary_search_descending(arrDes, N=len(arrDes), query=query))
    # print("our code binary search")
    # print(binary_search_ascending(arr, len(arr), query))
    # print("bisect_left code binary search")
    # print(bisect_left(arr, query))
    # print("bisect_right code binary search")
    # print(bisect_right(arr, query))

    # Output of above set for 11(exists)
    # our code binary search
    # 5
    # bisect_left code binary search
    # 5
    # bisect_right code binary search
    # 6

    # Output of above set for 24(not exists)
    # our code binary search
    # -1
    # bisect_left code binary search
    # 6
    # bisect_right code binary search
    # 6

