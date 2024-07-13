def matching(pattern, test, i, j):
    m, n = len(pattern), len(test)
    if j>=n:
        return i>=m
    if i>=m:
        return j>=n
    if pattern[i] != test[j] and pattern[i] != "*": # ? case is already taken care of above
        return False
    if pattern[i] == test[j] or pattern[i] == "?":
        return matching(pattern, test, i+1, j+1)
    if pattern[i] == "*":
        # This means that it can be matched with any pattern of length greater than or equal to 0
        # If this * is in the end, that means, it can match with all the characters of text
        if i==m-1:
            return True
        else:
            next = pattern[i+1]
            # Now we will move in text until we find a matching character to next or till end of test
            while j < n:
                if test[j] == next:
                    break
                j += 1 
            return matching(pattern, test, i+1, j)
    
    
def wildcardMatching(pattern, text):
    return matching(pattern, text, 0, 0)