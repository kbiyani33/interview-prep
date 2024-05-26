from typing import List
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