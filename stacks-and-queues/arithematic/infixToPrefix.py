def isOpenrand(s:str) -> bool:
    return s.isalnum()

def infixToPreFix(s:str) -> str:
    priorities = {
        "^": 3,
        "*": 2,
        "/": 2,
        "+": 1,
        "-": 1,
        "(": 0
    }
    result = []
    stack = []
    s = list(s)[::-1]
    for i in range(len(s)):
        if s[i] == "(":
            s[i] = ")"
        elif s[i] == ")":
            s[i] = "("
    
    for ch in s:
        if isOpenrand(ch):
            result.append(ch)
            continue
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            while stack and stack[-1] != "(":
                result.append(stack.pop())
            stack.pop() # removing the opening parenthesis as well
        else:
            if ch == "^":
                while stack and priorities[stack[-1]] > priorities[ch]: # because we cannot have 2 powers together
                    result.append(stack.pop())
            else:
                while stack and priorities[stack[-1]] >= priorities[ch]:
                    result.append(stack.pop())
            stack.append(ch)
    while stack:
        result.append(stack.pop())
    return "".join(result[::-1])

print(infixToPreFix("(a+b)*(c^d)"))

        