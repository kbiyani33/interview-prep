from typing import List

def getCowCount(stalls:List[int], ans):
    countOfCows = 1 # since i am placing the first cow at the first stall.
    n = len(stalls)
    previous = stalls[0]
    for i in range(1, n):
        if stalls[i] - previous >= ans:
            countOfCows += 1
            previous = stalls[i]
    return countOfCows

def aggressiveCows(stalls:List[int], k):
    stalls.sort()
    n = len(stalls)
    low, high = stalls[-1], stalls[n-1]-stalls[0]
    for i in range(n-1):
        low = min(low, stalls[i+1]-stalls[i])
    
    # minimum consecutive distance = low
    ans = -1
    while low <= high:
        mid = (low+high)//2

        # check if mid can be the minimum distance in between 2 cows
        countOfCows = getCowCount(stalls, mid)
        if countOfCows >= k:
            ans = mid
            # since we want maximum, i'll increase the ans
            low = mid+1
        else:
            high = mid-1
    return ans

