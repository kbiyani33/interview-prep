"""
Given a string, print the longest repeating subsequence such that, the two subsequence dont have same string character at same position.

Input: str = "aabb"
Output: "ab"

Input: str = "aab"
Output: "a"

The idea is that we will make 2 inputs st1 and st2

st1 = st
st2 = st

If we find the LCS of st1 and st2, we should get st only. However, we will make one small restriction in this.

In the dp matrix the if condition where st1[i-1] == st2[j-1] here i cannot be same as j since the equality is needed on different indicies

"""

def lengthOfLongestRepeatingSubsequence(st:str) -> int:
    m = len(st)
    dp = [[None]*(m+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(m+1):
            # base condition is when i=0 or j=0, we are basically getting LCS in bw 0 length ip and non zero length ip

            if i==0 or j==0:
                dp[i][j] = 0
            
            elif st[i-1] == st[j-1] and i!=j:
                dp[i][j] = 1 + dp[i-1][j-1]
                
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[-1][-1]
if __name__ == "__main__":
    st = "aabb"

    print(lengthOfLongestRepeatingSubsequence(st))