import heapq

import heapq

class SolutionBruteForce:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        minHeap = []
        for i in A:
            for j in B:
                sum_ij = i + j
                if len(minHeap) < C:
                    heapq.heappush(minHeap, sum_ij)
                else:
                    # Only push to heap if the current sum is larger than the smallest in the heap
                    if sum_ij > minHeap[0]:
                        heapq.heappushpop(minHeap, sum_ij)
        
        # Return the largest `C` sums in descending order
        return sorted(minHeap, reverse=True)


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        A.sort(reverse=True)
        B.sort(reverse=True)
        
        maxHeap = []
        visited = set()
        
        # Push the largest possible sum combination
        heapq.heappush(maxHeap, (-(A[0] + B[0]), 0, 0))
        visited.add((0, 0))
        
        result = []
        
        for _ in range(C):
            current_sum, i, j = heapq.heappop(maxHeap)
            result.append(-current_sum)
            
            # Push the next element from array A (i+1, j)
            if i + 1 < len(A) and (i + 1, j) not in visited:
                heapq.heappush(maxHeap, (-(A[i + 1] + B[j]), i + 1, j))
                visited.add((i + 1, j))
            
            # Push the next element from array B (i, j+1)
            if j + 1 < len(B) and (i, j + 1) not in visited:
                heapq.heappush(maxHeap, (-(A[i] + B[j + 1]), i, j + 1))
                visited.add((i, j + 1))
        
        return result