from typing import List


class Solution:
    # User function Template for python3

    # Complete this function
    def findFloor(self, A: List[int], N: int, X: int):
        start, end = 0, N - 1
        ans = -1
        while start <= end:
            mid = start + (end - start) // 2
            if A[mid] == X:
                return mid
            if A[mid] < X:
                ans = mid
                end = mid + 1
            else:
                start = mid - 1
        return ans
