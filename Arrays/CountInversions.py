from typing import List

import math

class Solution33:
    #User function Template for python3
    #Function to count inversions in the array.
    def mergeSortInversionCount(self, arr, low:int, high:int) -> int:
        if low >= high:
            return 0
        count = 0
        mid = low + (high-low)//2
        count += self.mergeSortInversionCount(arr, low, mid)
        count += self.mergeSortInversionCount(arr, mid+1, high)

        temp = []
        left, right = low, mid+1
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                count += mid - low + 1
                right += 1
        
        while left <= mid:
            temp.append(arr[left])
            left += 1
        
        while right <= high:
            temp.append(arr[right])
            right += 1
        
        return count

    def inversionCount(self, arr):
        n = len(arr)
        return self.mergeSortInversionCount(arr, 0, n-1)

class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def __init__(self):
        self.inversionCounter = 0

    def mergeSort(self, arr:List[int]):
        if len(arr) <= 1:
            return
        n = len(arr)
        mid = n//2
        leftHalf, rightHalf = arr[:mid], arr[mid:]

        self.mergeSort(leftHalf)
        self.mergeSort(rightHalf)

        i, j, k = 0, 0, 0
        while i<len(leftHalf) and j<len(rightHalf):
            if leftHalf[i] <= rightHalf[j]:
                arr[k] = leftHalf[i]
                i += 1
            else:
                # this is the case of inversions
                self.inversionCounter += len(leftHalf) - i
                arr[k] = rightHalf[j]
                j += 1
            k+=1
        while i<len(leftHalf):
            arr[k] = leftHalf[i]
            i+=1
            k+=1
        while j<len(rightHalf):
            arr[k] = rightHalf[j]
            j+=1
            k+=1

    def inversionCount(self, arr:List[int], n:int):
        # Your Code Here
        self.mergeSort(arr)
        return self.inversionCounter
    


soln = Solution33()
print(soln.inversionCount([2,4,1,3,5]))