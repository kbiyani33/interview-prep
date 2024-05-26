from typing import List


class Solution:
    def BetterSolutionInPython(self, arr: List[int], n: int, x: int):
        arr.sort()  # NlogN
        left, right = 0, n - 1
        while left < right:
            sumLR = arr[left] + arr[right]
            if sumLR == x:
                return True
            if sumLR > x:
                # we will go towards a smaller value, so decrement right
                right -= 1
            else:
                left += 1
        return False

    def BestInPythonMightNotInCpp(self, arr: List[int], n: int, x: int):
        val = {}
        for i in range(n):

            if x - arr[i] in val:
                return True
            val[arr[i]] = i

        return False
