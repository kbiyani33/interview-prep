from typing import List
class Solution:
    def Better(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for i in range(len(nums)):
            hashTable = {}
            for j in range(i+1, len(nums)):
                third = -1 * (nums[i]+nums[j])
                if third in hashTable: # we got a possible triplet
                    res = [nums[i], nums[j], third]
                    res.sort()
                    ans.add(tuple(res))
                hashTable[nums[j]] = True
        return [list(i) for i in ans]
    

    def optimal(self, nums:List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        i, j, k = 0, 1, n-1
        while i<n:
            while j<k:
                curSum = nums[i]+nums[j]+nums[k]
                if curSum > 0:
                    k-=1
                elif curSum < 0:
                    j+=1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    curK, curJ = nums[k], nums[j]
                    while(True):
                        if k>=0 and nums[k]==curK:
                            k-=1
                        else:
                            break
                    while True:
                        if j<n and nums[j]==curJ:
                            j+=1
                        else:
                            break
            curI = nums[i]
            while True:
                if i<n and nums[i]==curI:
                    i+=1
                else:
                    break
            j = i+1
            k = n-1
        
        return ans
                
                    