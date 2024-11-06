from typing import List

class Solution:
    def trapOptimal(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        lmax, rmax = 0, 0
        water = 0
        while left < right:
            if height[left] <= height[right]:
                if lmax > height[left]:
                    water += lmax - height[left]
                else:
                    lmax = height[left]
                left += 1
            else:
                if rmax > height[right]:
                    water += rmax - height[right]
                else:
                    rmax = height[right]
                right -= 1
        return water
            


class Solution:
    def trapNonOptimalOnSpace(self, height: List[int]) -> int:
        n = len(height)
        prefixMatch = [0] * n
        suffixMatch = [0] * n

        # Fill prefixMatch array
        prefixMatch[0] = height[0]
        for i in range(1, n):
            prefixMatch[i] = max(prefixMatch[i-1], height[i])

        # Fill suffixMatch array
        suffixMatch[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            suffixMatch[i] = max(suffixMatch[i+1], height[i])
        water = 0
        for i in range(n):
            water += min(prefixMatch[i], suffixMatch[i]) - height[i]
        return water