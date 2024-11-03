class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        opening = brackets.keys()
        closing = brackets.values()
        for i in s:
            if i not in closing and i not in opening:
                continue
            if i in opening:
                stack.append(i)
            elif i in closing:
                if not stack or i != brackets[stack[-1]]: # cannot have closing before any opening
                    return False
                stack.pop()
        # print(stack)
        return len(stack) == 0
        