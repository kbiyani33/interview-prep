from typing import List

def selectionSort(arr:List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        minIndex = -1
        minVal = arr[i]
        for j in range(i+1, n):
            if arr[j] < minVal:
                minVal = arr[j]
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr



if __name__=="__main__":
    arr = [13, 46, 24, 52, 20, 9]
    selectionSort(arr)
    print(arr)