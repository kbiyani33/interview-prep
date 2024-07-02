def recursivePartition(string:str, index:int, dp) -> int:
    n = len(string)
    if index==n:
        return 0
    if dp[index] != -1:
        return dp[index]
    temp = ""
    minI = n # I can get at max n-1 partitions in a string where all partitions are of the length 1
    for j in range(index, n):
        temp += string[j]
        if temp == temp[::-1]: # Palindrome
            ans = 1 + recursivePartition(string, j+1, dp)
            minI = min(ans, minI)
    dp[index] = minI
    return minI

def tabulationBottomUpDP(string:str) -> int:
    # Step 1
    n = len(string)
    dp = [0]*(n+1)
    for i in range(n-1, -1, -1):
        # what is this i? The index from which I am starting the partitions
        temp = ""
        minI = n # I cannot have more than n-1 partitions anyway
        for j in range(i, n):
            temp += string[j]
            if temp==temp[::-1]:
                ans = 1 + dp[j+1]
                minI = min(minI, ans)
        dp[i] = minI
    return dp[0]-1

def palindromePartitioning(string: str) -> int:
    # Write your code here.
    dp = [-1]*(len(string)+1)
    return recursivePartition(string, 0, dp)-1 # we need to subtract this 1 since we are doing an empty partition in the end which is not allowed, since we want non-empty partititons
