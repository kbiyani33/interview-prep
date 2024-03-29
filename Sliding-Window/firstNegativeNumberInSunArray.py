"""
The idea is that I'll keep a list of only negative numbers. 
When I hit a window, then i'll simply return the first element in the negative number list.

But suppose the window of size 2 is like [7, -8] then negative element list will have -8.

start is at 7 and end is at -8. I'll return -8

But because my element at start index is not the same as negative element returned,
We don't delete anything in negative number list.
"""

from typing import List

def firstNegativeNumber(arr:List[int], N:int, K:int) -> List[int]:
    start, end = 0, 0
    negative_numbers_watch = []
    op = []
    while(end < N):
        if arr[end] < 0:
            negative_numbers_watch.append(arr[end])
        if end-start+1 < K:
            end += 1
        elif end-start+1 == K:
            # we have a window so we will get the first negative number
            if len(negative_numbers_watch) > 0:
                # Suppose the window is like [7, -8]
                op.append(negative_numbers_watch[0])
                negative_numbers_watch = negative_numbers_watch[1:] if arr[start] == negative_numbers_watch[0]  else negative_numbers_watch
            else:
                op.append(0)
            
            end += 1
            start += 1
    return op

if __name__=="__main__" :
    arr = [12, 7, -8, -8, -1, 4, 6, -13, 11]
    K = 2
    # op = maximum_sum_subarray_size(arr, len(arr), K)
    op = firstNegativeNumber(arr, N=8, K=K)
    print(op)