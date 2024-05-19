from typing import *


def sortedArray(a: List[int], b: List[int]) -> List[int]:
    # Write your code here
    m, n = len(a), len(b)
    ans = []
    i, j = 0, 0

    while i < m and j < n:
        if a[i] <= b[j]:
            if (len(ans) > 0 and ans[-1] != a[i]) or len(ans) == 0:
                ans.append(a[i])
            i += 1
        elif a[i] > b[j]:
            if (len(ans) > 0 and ans[-1] != b[j]) or len(ans) == 0:
                ans.append(b[j])
            j += 1

    while j < n:
        if (len(ans) > 0 and ans[-1] != b[j]) or len(ans) == 0:
            ans.append(b[j])
        j += 1

    while i < m:
        if (len(ans) > 0 and ans[-1] != a[i]) or len(ans) == 0:
            ans.append(a[i])
        i += 1

    return ans


from os import *
from sys import *
from collections import *
from math import *


def findArrayIntersection(arr: list, n: int, brr: list, m: int):
    # Write your code here
    ans = []
    m, n = len(arr), len(brr)
    i, j = 0, 0
    while i < m and j < n:
        if arr[i] == brr[j]:
            ans.append(arr[i])
            i += 1
            j += 1
        elif arr[i] < brr[j]:
            i += 1
        else:
            j += 1
    # Return a list containing all the common elements in arr and brr.
    return ans
