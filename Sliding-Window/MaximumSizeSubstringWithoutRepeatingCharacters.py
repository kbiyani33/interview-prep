"""
In any problem using subsequence etc, we need to start thinking about the 2 pointer sliding window
"""
class Solution:
    def slidingWindowSolution(self, s:str) -> int:
        n = len(s)
        maxLen = 0
        left, right = 0, 0
        hashTable = {}
        while right < n:
            if s[right] in hashTable and left <= hashTable[s[right]]:
                left = hashTable[s[right]]+1
            subStrlen = right-left+1
            maxLen = max(maxLen, subStrlen)
            hashTable[s[right]] = right
            right += 1
        return maxLen
    def bruteForceSolution(self, s:str) -> int:
        # TC = O(N^2)
        # SC = O(len(s))
        n = len(s)
        maxLen = 0
        for i in range(n):
            hashTable = {}
            for j in range(i, n):
                if s[j] in hashTable:
                    break
                length = j-i+1
                maxLen = max(maxLen, length)
                hashTable[s[j]] = True
        return maxLen
 
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.bruteForceSolution(s)

if __name__=="__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))