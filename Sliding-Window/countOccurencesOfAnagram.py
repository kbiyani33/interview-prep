"""
Given a word pat and a text txt. 
Return the count of the occurrences of anagrams of the word in the text.

Example 1:

Input:
txt = forxxorfxdofr
pat = for
Output: 3
Explanation: for, orf and ofr appears
in the txt, hence answer is 3.
Example 2:

Input:
txt = aabaabaa
pat = aaba
Output: 4
Explanation: aaba is present 4 times
in txt.
"""

def getCharacterFrequency(query:str) -> dict: # type: ignore
    op = {}
    for i in query:
        if i in op:
            op[i] += 1
        else:
            op[i] = 1
    # print(op)
    return op

def countAnagramsBruteForce(query:str, pattern:str) -> int:
    counter = 0
    N = len(query)
    K = len(pattern)
    pattern_char_freq = getCharacterFrequency(pattern)
    for i in range(N):
        if i+K > N:
            break
        substr = query[i:i+K]
        print(substr)
        if getCharacterFrequency(substr) == pattern_char_freq:
            counter += 1
    return counter

def countAnagrams(query:str, pattern:str) -> int:
    N = len(query)
    K = len(pattern)
    pattern_char_freq = getCharacterFrequency(pattern)
    distinct_char_count = len(pattern_char_freq.keys())
    counter = 0
    start, end = 0, 0

    while(end<N):
        if query[end] in pattern_char_freq:
            pattern_char_freq[query[end]] -= 1
            if pattern_char_freq[query[end]] == 0:
                distinct_char_count -= 1 # basically distinct count has become 0
        
        if end-start+1 < K:
            end += 1
        elif end-start+1 == K:
            if distinct_char_count == 0:
                counter += 1
            if query[start] in pattern_char_freq.keys():
                pattern_char_freq[query[start]] += 1
                if pattern_char_freq[query[start]] == 1: # this means that it has become from 0 to 1 so now it's distinct count should increase. Note that it won't be increased when the value after increment becomes 2, 3, ...
                    distinct_char_count += 1
            start += 1
            end += 1
    return counter

if __name__ == "__main__":
    inputTxt = "aabaabaa"
    search = "aaba"
    print(countAnagrams(inputTxt, search))
