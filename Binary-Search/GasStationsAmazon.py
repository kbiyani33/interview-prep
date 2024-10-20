from typing import List
import heapq


def minimiseMaxDistanceBruteForce(arr: List[int], k: int) -> float:
    n = len(arr)
    positions = [0 for _ in range(n-1)]

    for gasStations in range(k):
        # get the maximum distance
        maxDist, maxDisIndex = -1, -1
        for i in range(n-1):
            diff = arr[i+1] - arr[i]
            length = diff / (positions[i]+1)

            if length > maxDist:
                maxDist = length
                maxDisIndex = i
        
        positions[maxDisIndex] += 1
    
    maxAns = -1
    for i in range(n-1):
        diff = arr[i+1] - arr[i]
        length = diff/(positions[i]+1)
        maxAns = max(maxAns, length)
    return maxAns

import heapq

def minimiseMaxDistance(arr:List[int], k: int) -> float:
    heap = []
    n = len(arr)
    placed = [0] * (n - 1)

    # Initialize the heap with initial gaps
    for i in range(n - 1):
        diff = arr[i + 1] - arr[i]
        heapq.heappush(heap, (-diff, i))
    
    # Add k gas stations
    for _ in range(k):
        # Get the largest gap
        negDiff, index = heapq.heappop(heap)
        diff = -negDiff

        # Increment the number of divisions for this segment
        placed[index] += 1

        # Calculate the new maximum segment length
        newDiff = (arr[index+1]-arr[index]) / (placed[index] + 1)

        # Push the new gap back into the heap
        heapq.heappush(heap, (-newDiff, index))
    
    # The maximum distance after adding k gas stations
    maxDiff, _ = heapq.heappop(heap)
    return -maxDiff

def getCountOfGasStationsAtMaxDistance(arr:List[int], ans:int) -> int:
    count = 0
    for i in range(len(arr) - 1):
        inBetweenDiff = arr[i+1] - arr[i]
        quotient = inBetweenDiff / ans
        if inBetweenDiff % ans == 0.0:
            count += quotient - 1
        else:
            count += int(quotient)
    return count

def minimiseMaxDistanceOptimal(arr: List[int], k: int) -> float:
    low, high = 0, arr[-1]
    n = len(arr)
    for i in range(n-1):
        high = max(high, arr[i+1]-arr[i])
    
    epsilon = 1e-6
    
    while high - low > epsilon:
        mid = (low + high) / 2.0

        countMid = getCountOfGasStationsAtMaxDistance(arr, mid)
        
        if countMid > k:
            low = mid
        else:
            high = mid
    return high


print(minimiseMaxDistanceBruteForce(arr=[4,6,10], k=4))
print(minimiseMaxDistance(arr=[4,6,10], k=4))