from typing import List

def getFirstOccurence(arr:List[int], query:int) -> int:
    result = -1
    n = len(arr)
    start, end = 0, n-1
    while(start <= end):
        middle = start + (end-start)//2
        if arr[middle] == query:
            result = middle
            end = middle - 1
            continue

        if query > arr[middle]:
            start = middle + 1
        else:
            end = middle -1
    return result

def getLastOccurence(arr:List[int], query:int) -> int:
    result = -1
    n = len(arr)
    start, end = 0, n-1
    while(start <= end):
        middle = start + (end-start)//2

        if arr[middle] == query:
            result = middle
            start = middle + 1
            continue

        if query > arr[middle]:
            start = middle + 1
        else:
            end = middle -1
    return result
        

def countOccurences(arr:List[int], query:int) -> int:
    first = getFirstOccurence(arr, query)
    last = getLastOccurence(arr, query)
    if first == -1 and last == -1:
        return 0
    return last-first+1

if __name__ == "__main__":
    arr = [2, 4, 5, 6, 8, 11, 11, 11, 11, 32, 43]
    query = 11
    print(countOccurences(arr, query))
