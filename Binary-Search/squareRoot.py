class Solution:
    def mySqrt(self, x: int) -> int:
        if x<= 0 :
            return x
        low, high = 1, x
        while low<=high:
            mid = low + (high-low)//2
            if mid <= x/mid: low = mid+1
            else: high = mid-1
        return high