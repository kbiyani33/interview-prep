#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here
        n = len(arr)
        arr.sort()
        dep.sort()
        
        left, right = 0, 0
        maxCount = 0
        count = 0
        while left < n and right < n:
            if arr[left] <= dep[right]:
                count += 1
                maxCount = max(count, maxCount)
                left += 1
            else:
                count -= 1
                right += 1
        # if only arrivals are remaining now
        return maxCount