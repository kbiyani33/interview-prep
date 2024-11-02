from typing import List
from math import inf

class TrieNode:
    def __init__(self):
        self.children = [None, None]

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, val:int) -> None:
        node = self.root
        for i in range(31, -1, -1):
            # get the i'th bit value
            bit = (val >> i) & 1
            if not node.children[bit]:
                node.children[bit] = TrieNode()
            node = node.children[bit]
        node.numberEndingHere = True
        return
    
    def maximiseXorValue(self, val:int) -> int:
        node = self.root
        maxXor = 0
        for i in range(31, -1, -1):
            bit = (val >> i) & 1
            oppBit = 1 - bit
            if node.children[oppBit]:
                node = node.children[oppBit]
                maxXor = (maxXor << 1) | 1
            else:
                node = node.children[bit]
                maxXor = (maxXor << 1)
        return maxXor


class Solution:
    def maxSubarrayXOR (self, N:int, arr:List[int]):
        # code here
        
        trie = Trie()
        trie.insert(0) # for initial calculations we will insert prefixXor[i]
        maxXor = 0
        prefixXorSoFar = 0

        for i in range(N):
            prefixXorSoFar ^= arr[i]
            queryResult = trie.maximiseXorValue(prefixXorSoFar)
            maxXor = max(maxXor, queryResult)
            trie.insert(prefixXorSoFar)

        return maxXor