from collections import Counter
from typing import List


class Solution:
    def dutchNationalFlagAlgorithm(self, arr: List[int]) -> None:
        low, mid, high = 0, 0, len(arr) - 1
        while True:
            if mid > high:
                break
            if arr[mid] == 0:
                arr[mid], arr[low] = arr[low], arr[mid]
                mid += 1
                low += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

    def better(self, nums: List[int]) -> None:
        freq = Counter(nums)
        nums[:] = [0] * freq[0] + [1] * freq[1] + [2] * (freq[2])

    def brute(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()

    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(arr) - 1
        while True:
            if mid > high:
                break
            if arr[mid] == 0:
                arr[mid], arr[low] = arr[low], arr[mid]
                mid += 1
                low += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
