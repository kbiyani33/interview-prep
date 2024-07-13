from typing import List


class Solution:
    # User function Template for python3

    # Complete this function
    def getFloorAndCeil(self, A: List[int], N: int, X: int):
        A.sort()
        start, end = 0, N - 1
        floor, ceil = -1, -1
        while start <= end:
            mid = start + (end - start) // 2
            if A[mid] == X:
                return [mid, mid]
            if A[mid] < X:
                floor = mid
                end = mid + 1
            else:
                ceil = mid
                start = mid - 1
        return [floor, ceil]


class Solution:
    def count(self, nums: List[int], target: int) -> List[int]:
        def firstOccurence(nums, target):
            res = -1
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] == target:
                    res = mid
                    end = mid - 1
                elif target < nums[mid]:
                    end = mid - 1
                elif target > nums[mid]:
                    start = mid + 1
            return res

        def lastOccurence(nums, target):
            res = -1
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] == target:
                    res = mid
                    start = mid + 1
                elif target < nums[mid]:
                    end = mid - 1
                elif target > nums[mid]:
                    start = mid + 1
            return res

        first = firstOccurence(nums, target)
        last = lastOccurence(nums, target)
        if first == -1 or last == -1:
            return 0
        return last - first + 1
