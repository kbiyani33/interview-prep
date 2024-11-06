from typing import List, Optional
from heapq import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0:
            return None
        if k==1:
            return lists[0]
        dummy = ListNode(-1)
        minHeap = []
        for i in range(k):
            if not lists[i]:
                continue
            heappush(minHeap, (lists[i].val, i, lists[i]))
        curr = dummy
        while minHeap:
            val, index, listnode = heappop(minHeap)
            curr.next = ListNode(val)
            curr = curr.next
            if listnode.next:
                heappush(minHeap, (listnode.next.val, index, listnode.next))
        return dummy.next