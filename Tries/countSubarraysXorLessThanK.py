from typing import List

class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, x: int):
        node = self.root
        for i in range(31, -1, -1):
            bit = (x >> i) & 1
            if not node.children[bit]:
                node.children[bit] = TrieNode()
            node = node.children[bit]
            node.count += 1
    
    def countLessThanThreshold(self, x: int, k: int) -> int:
        count = 0
        node = self.root
        for i in range(31, -1, -1):
            if not node:
                break
            x_bit = (x >> i) & 1
            k_bit = (k >> i) & 1
            if k_bit == 1:
                # If k_bit is 1, we can choose the subtrees that have x_bit
                if node.children[x_bit]:
                    count += node.children[x_bit].count
                # Move to the subtree with x_bit == 1
                node = node.children[1 - x_bit]
            else:
                # Move to the subtree with x_bit
                node = node.children[x_bit]
        return count

def countSubarrayXorLessThanK(n: int, arr: List[int], k: int) -> int:
    count = 0
    prefXor = 0
    trie = Trie()
    trie.insert(0)
    for num in arr:
        prefXor ^= num
        # Count subarrays with XOR < k
        count += trie.countLessThanThreshold(prefXor, k)
        trie.insert(prefXor)
    return count

if __name__ == "__main__":
    n,k = [int(i) for i in input().strip().split(" ")]
    arr = [int(i) for i in input().strip().split(" ")]
    print(countSubarrayXorLessThanK(n, arr, k))
