from typing import List
class Solution:
    def totalFruits(self,arr:List[int]) -> int:
        n = len(arr)
        fruitmap = {}
        left, right = 0, 0
        maxLen = 0
        while right < n:
            val = arr[right]
            if val in fruitmap:
                fruitmap[val] += 1
            else:
                fruitmap[val] = 1
                if len(fruitmap) > 2:
                    # start deleting from left
                    while left<=right:
                        if len(fruitmap) ==2:
                            break
                        fruitmap[arr[left]] -= 1
                        if fruitmap[arr[left]]==0:
                            del fruitmap[arr[left]]
                        left += 1
            maxLen = max(maxLen, right-left+1)
            right += 1
        
        return maxLen

