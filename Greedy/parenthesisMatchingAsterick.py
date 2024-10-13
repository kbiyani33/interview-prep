from typing import List

class Solution:
    def recursive(self, s:str, index:int, counter:List[int], dp):
        if counter < 0:
            return False
        if index == len(s):
            return counter == 0
        if dp[index][counter] != -1:
            return dp[index][counter]
        if s[index] == "(":
            ans = self.recursive(s, index+1, counter+1, dp)
        elif s[index] == ")":
            ans = self.recursive(s, index+1, counter-1, dp)
        elif s[index] == "*":
            ans1 = self.recursive(s, index+1, counter+1, dp)
            ans2 = self.recursive(s, index+1, counter-1, dp)
            ans3 = self.recursive(s, index+1, counter, dp)
            ans = ans1 or ans2 or ans3
        dp[index][counter] = ans
        return ans
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        return self.recursive(s, 0, 0, dp)

# optimal
class Solution:
    def checkValidString(self, s: str) -> bool:
        m1, m2 = 0, 0
        if s and (s[0] == ")" or s[-1] == "("): return False
        for i in s:
            if i=="(":
                m1 += 1
                m2 += 1
            elif i==")":
                m1 -= 1
                m2 -= 1
            else:
                m1 -= 1
                m2 += 1
            if m1 < 0: m1=0
            if m2 < 0: return False # too many closing parenthesis
        return m1==0

