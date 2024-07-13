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
