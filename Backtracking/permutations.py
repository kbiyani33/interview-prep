from typing import List

class Solution:
    def permute(self, nums: List[any]) -> List[List[any]]:
        def recursive(index:int, permutation:List[any]) -> None:
            if len(permutation) == len(nums):
                result.append(permutation[:])
                return
            for i in range(len(nums)):
                if i == index or visited[i] == 1:
                    continue
                permutation.append(nums[i])
                visited[i] = 1
                recursive(i, permutation)
                permutation.pop()
                visited[i] = 0
        result = []
        visited = [0 for _ in range(len(nums))]
        recursive(-1, [])
        return result
    
if __name__ == "__main__":
    soln = Solution()
    print(soln.permute([1,2,3]))
    print(soln.permute([1,1,2,3]))
    print(soln.permute(["a", "b", "c"]))
        

