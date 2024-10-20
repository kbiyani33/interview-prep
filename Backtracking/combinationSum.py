from typing import List

class Solution:
    def recursive(self, candidates: List[int], target: int, index:int, current:List[int], result:List[List[int]]):
        if index == len(candidates) or target < 0:
            return
        if target == 0:
            result.append(current[:])
            return
        # print(index, target)
        # 2 possibilities either current one can be taken or it cannot
        self.recursive(candidates, target, index+1, current, result)
        
        current.append(candidates[index])
        self.recursive(candidates, target-candidates[index], index, current, result)
        current.pop() # backtracking

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # edge cases is if candidates is empty or target is 0
        if not candidates or target==0:
            return []
        allCombinations = []
        # candidates.sort(reverse=True) # since i am sorting, i can only move forward without worrying about previous values since if current index is not valid, none of the previous indices will be valid
        for i in range(len(candidates)):
            if candidates[i] > target:
                continue
            self.recursive(candidates, target-candidates[i], i, [candidates[i]], allCombinations)
        return allCombinations