from typing import List
class Solution:
    def bruteForce(self, arr: List[int], k: int) -> int:
        for num in arr:
            if num>k:
                return k
            k += 1
        return k