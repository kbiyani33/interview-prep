from typing import List
class Solution:
    def fourSumBetter(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = set()
        for i in range(n):
            for j in range(i+1, n):
                hashTable = {}
                for k in range(j+1, n):
                    fourth = target - (nums[i]+nums[j]+nums[k])
                    if fourth in hashTable:
                        quad = [nums[i], nums[j], nums[k], fourth]
                        quad.sort()
                        ans.add(tuple(quad))
                    hashTable[nums[k]] = True
        
        return [list(i) for i in ans]
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans, n = [], len(nums)
        nums.sort()
        i, j, k, l = 0, 1, 2, n-1
        while i<n:
            j = i+1
            while j<n:
                k = j+1
                l = n-1
                while k<l:
                    curSum = nums[i]+nums[j]+nums[k]+nums[l]
                    if curSum>target:
                        l-=1
                    elif curSum<target:
                        k+=1
                    else:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        curK, curL = nums[k], nums[l]
                        while k<l and nums[k]==curK:
                            k+=1
                        while k<l and nums[j]==curL:
                            l-=1
                curJ = nums[j]
                while j<n and nums[j]==curJ:
                    j+=1
            curI = nums[i]
            i+=1
            while i<n and nums[i]==curI:
                i+=1
        return ans
        