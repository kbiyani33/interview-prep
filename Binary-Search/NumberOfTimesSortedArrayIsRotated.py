"""
Find the Rotation Count in Rotated Sorted array
Consider an array of distinct numbers sorted in increasing order. The array has been rotated (clockwise) k number of times. Given such an array, find the value of k.

Examples:

Input : arr[] = {15, 18, 2, 3, 6, 12}
Output: 2
Explanation : Initial array must be {2, 3,
6, 12, 15, 18}. We get the given array after 
rotating the initial array twice.

Input : arr[] = {7, 9, 11, 12, 5}
Output: 4

Input: arr[] = {7, 9, 11, 12, 15};
Output: 0
"""

# The index of the minimum element is the number of times it had been rotated
from typing import List

def numberOfRotations(arr:List[int]) -> int:
    N = len(arr)
    start, end = 0, N-1
    result = -1
    while(start <= end):
        middle = start + (end-start)//2
        next = (middle+1)%N
        previous = (middle + N - 1)%N
        if arr[middle] < arr[next] and arr[middle] < arr[previous]:
            result = middle
            break
        # move towards unsorted array
        elif arr[start] < arr[middle]:
            start = middle+1
        elif arr[middle] < arr[end]:
            end = middle-1
    return result
    
        

if __name__ == "__main__":
    arr = [43, 32, 2, 4, 5, 6, 8, 11]
    print(numberOfRotations(arr))
