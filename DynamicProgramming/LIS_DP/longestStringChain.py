def is_predecessor(s1, s2):
    # Check if s2 is a predecessor of s1
    if len(s1) != len(s2) + 1:
        return False

    first = 0
    second = 0

    while first < len(s1):
        if second < len(s2) and s1[first] == s2[second]:
            first += 1
            second += 1
        else:
            first += 1

    return first == len(s1) and second == len(s2)


def longestStrChain(arr):
    n = len(arr)

    # Sort the array in ascending order of string length
    arr.sort(key=len)

    dp = [1] * n
    maxi = 1

    for i in range(n):
        for prev_index in range(i):
            if is_predecessor(arr[i], arr[prev_index]) and 1 + dp[prev_index] > dp[i]:
                dp[i] = 1 + dp[prev_index]

        if dp[i] > maxi:
            maxi = dp[i]

    return maxi