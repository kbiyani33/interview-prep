from typing import *

def mergeTwoSortedArraysWithoutExtraSpace(a : List[int], b : List[int]) -> int:
    # Write your code here.
    n, m = len(a), len(b)
    length = m+n
    gap = int((length//2) + (length%2))

    while True:
        left, right = 0, gap
        while right < length:
            if right < n:
                # both in a
                if a[right] < a[left]:
                    a[left], a[right] = a[right], a[left]
            elif left < n and right >= n:
                # left in a and right in b
                if b[right-n] < a[left]:
                    b[right-n], a[left] = a[left], b[right-n]
            elif left >= n:
                # both in b
                if b[right-n]<b[left-n]:
                    b[right-n],b[left-n]=b[left-n],b[right-n]
            left += 1
            right += 1
        
        if gap == 1:
            break
        gap = int((gap//2) + (gap%2))