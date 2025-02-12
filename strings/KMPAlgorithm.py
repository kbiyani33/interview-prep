def kmpStringMatch(pattern:str, text:int) -> int:
    m, n = len(text), len(pattern)
    F = [0]*n
    # preprocess the prefix table of pattern
    j = 0
    for i in range(1, n):
        while j>0 and pattern[i] != pattern[j]:
            j = F[j-1]
        if pattern[i]==pattern[j]:
            j += 1
        F[i] = j
        


if __name__=="__main__":
    pattern = "abcaa"
    text = "bdcabcaabcabcaa"
    print(kmpStringMatch(pattern, text))