"""
Given an array of integers A.  There is a sliding window of size B which 

is moving from the very left of the array to the very right. 

You can only see the w numbers in the window. Each time the sliding window moves 

rightwards by one position. You have to find the maximum for each window. 

The following example will give you more clarity.

The array A is [1 3 -1 -3 5 3 6 7], and B is 3.

Window position	Max
———————————-	————————-
[1  3  -1] -3  5  3  6  7	3
1 [3  -1  -3] 5  3  6  7	3
1  3 [-1  -3  5] 3  6  7	5
1  3  -1 [-3  5  3] 6  7	5
1  3  -1  -3 [5  3  6] 7	6
1  3  -1  -3  5 [3  6  7]	7
Return an array C, where C[i] is the maximum value of from A[i] to A[i+B-1].

Note: If B > length of the array, return 1 element with the max of the array. 
"""
from typing import List
from collections import deque

def solutionCode(ip:List[int], k:int) -> List[int]:
    op = []
    start,end = 0,0
    N = len(ip)
    q = deque()
    while(end<N):
        while(len(q) > 0 and ip[end] > q[0]):
            removed = q.popleft()
            print("removed ", removed)
        print("q ", q)
        q.append(ip[end])
        print("q ", q)
        
        if end-start+1 != k:
            end += 1
        elif end-start+1 == k:
            op.append(q[0]) # the maximum has to be in the top of the deque
            if ip[start] == q[0]:
                q.popleft()
            start += 1
            end += 1
    return op

if __name__ == "__main__":
    input = [ 268, 202, 139, 744, 502, 582, 94, 81, 117, 258, 506, 461, 531, 768, 827, 128, 592, 571, 559, 374, 910, 610, 561, 489, 647, 246, 355, 313, 158, 922, 557, 36, 430, 983, 913, 303, 765, 945, 167, 340, 869, 869, 609, 809, 529, 715, 34, 13, 657, 407, 684, 801, 129, 952, 159, 250, 546, 508, 540, 948, 429, 174 ]
    K = 3
    print(solutionCode(input, K))