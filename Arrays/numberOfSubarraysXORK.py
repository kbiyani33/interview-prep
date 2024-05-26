from collections import defaultdict
from typing import List

def subarraysWithSumK(A:List[int], B:int) -> int:
    prefixXor, prefixXorMap = 0, defaultdict(int)
    ans = 0
    for i in range(len(A)):
        prefixXor ^= A[i]
        if prefixXor == B:
            ans += 1
        # We are not finding any longest or something else. So if we have a middle element having B^prefixXor, we need that as well. 
        # One tricky case is when the xor so far is equal to K. So this can occur by xor'ing all till now which will be 1 case, or there may have been a 0 xor in between somehow, 
        # so we want to count the subarray from that index to current index as separate subarray.
        ans += prefixXorMap[B^prefixXor]
        prefixXorMap[prefixXor] += 1
    
    return ans