def isOpenrand(s:str) -> bool:
    return s.isalnum()

def infixToPostFix(s:str) -> str:
    priorities = {
        "^": 3,
        "*": 2,
        "/": 2,
        "+": 1,
        "-": 1,
    }
    result = []
    stack = []
    
    for ch in s:
        if isOpenrand(ch):
            result.append(ch)
            continue
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            while stack and stack[-1] != "(":
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != "(" and priorities[stack[-1]] >= priorities[ch]: # it's possible that we have operators before the closing parenthesis, so we have to make sure tht we are closing it till openinig parenthesis
                result.append(stack.pop())
            stack.append(ch)
    
    while stack:
        result.append(stack.pop())
    return "".join(result)

print(infixToPostFix("(a+b)*(c^d)"))

        