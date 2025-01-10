from collections import Counter
from typing import List, Dict

def generatePermutations(st:str) -> List[str]:
    def recursive(permutation:List[str]) -> None:
        if len(permutation) == len(st):
            result.append("".join(permutation))
            return
        for i in range(n):
            if visited[i] == 1:
                continue
            permutation.append(st[i])
            visited[i] = 1
            recursive(permutation)
            visited[i] = 0 # backtracking
            permutation.pop() # backtracking
            
    result = []
    n = len(st)
    visited = [0]*n
    recursive([])
    return result
    

def validateForPalindrome(freqMap:Dict[str, int]):
    oddCount = 0
    for ch in freqMap:
        if not freqMap[ch] & 1:
            continue
        oddCount += 1
        if oddCount > 1: return False
            
    return True

def palidromicPermutations(st:str) -> List[str]:
    # step 1 is to verify if it's possible to even make palindromic permutations :)
    freqMap = Counter(st)
    validString = validateForPalindrome(freqMap)
    if not validString:
        print("invalid string for palidromic permutations")
        return []
    """
    Now there are basically 2 cases, either the number of characters is even or it's odd
    if it's odd, then the map is like this:
    a:2, b:2, c:3
    if it's odd, then the map is like this:
    a:2, b:2, c:2
    Then what we will have to do is take half(integer division)
    """
    halfString = []
    for ch in freqMap:
        for _ in range(int(freqMap[ch]/2)):
            halfString.append(ch)
    # I will need if there is any odd character
    oddChar = [i for i in freqMap if freqMap[i] & 1]
    # now i will generate all the permutations of half string
    allPermutationsOfHalfString = generatePermutations(halfString)
    result = []
    # now we will go into each permutation and simply add the remaining half to the permutation
    for permutation in allPermutationsOfHalfString:
        if oddChar:
            result.append(permutation + oddChar[0] + permutation[::-1])
        else:
            result.append(permutation + permutation[::-1])
    return result
        

if __name__=="__main__":
    # print(generatePermutations("abcd"))
    print(palidromicPermutations(st = "abc"))