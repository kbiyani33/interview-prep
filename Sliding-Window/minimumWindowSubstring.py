from math import inf
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tFreqMap = {}
        for i in t:
            if i not in tFreqMap:
                tFreqMap[i] = 0
            tFreqMap[i] += 1
        
        m, n = len(t), len(s)
        left, right = 0, 0
        minLength, startIndex, count = inf, -1, 0
        while right < n:
            if s[right] not in tFreqMap:
                tFreqMap[s[right]] = -1
                continue
            if tFreqMap[s[right]] > 0:
                count += 1
            tFreqMap[s[right]] -= 1

            while count==m:
                if right-left+1 < minLength:
                    minLength = right-left+1
                    startIndex = left
                tFreqMap[s[left]] +=1
                if tFreqMap[s[left]] > 0:
                    count -= 1
                left += 1
            right += 1
        # print(minLength, startIndex)
        if startIndex == -1:
            return ""
        return s[startIndex:startIndex+minLength]
        # return "" if startIndex==-1 else return s[startIndex:startIndex+minLength]


            

            