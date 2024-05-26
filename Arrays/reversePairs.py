from typing import List

class Solution:
    def __init__(self):
        self.reversePairCounter = 0

    def mergeSort(self, nums:List[int]):
        n = len(nums)
        if n<=1:
            return
        mid = n//2
        leftHalf, rightHalf = nums[:mid], nums[mid:]
        self.mergeSort(leftHalf)
        self.mergeSort(rightHalf)
        # Now that we have come here means that we have the left and right sorted portions
        # Lets count that for how many in left, does the condition satisfy !!!
        i,j = 0,0
        for i in range(len(leftHalf)):
            while j<len(rightHalf) and leftHalf[i] > 2*rightHalf[j]:
                j+=1
            self.reversePairCounter += j
        # Now lets perform the merge
        i, j, k = 0, 0, 0
        while i<len(leftHalf) and j<len(rightHalf):
            if leftHalf[i] <= rightHalf[j]:
                nums[k] = leftHalf[i]
                i+=1
            else:
                nums[k] = rightHalf[j]
                j+=1
            k+=1
        while i<len(leftHalf):
            nums[k] = leftHalf[i]
            i+=1
            k+=1
        while j<len(rightHalf):
            nums[k]=rightHalf[j]
            j+=1
            k+=1


    def reversePairs(self, nums: List[int]) -> int:
        self.mergeSort(nums)
        return self.reversePairCounter