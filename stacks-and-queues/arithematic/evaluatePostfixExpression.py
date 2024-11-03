from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = len(tokens)
        for i in range(n):
            ch = tokens[i]
            if ch.lstrip("-").isnumeric():
                stack.append(int(ch))
            else:
                # print(stack)
                t1 = stack.pop()
                t2 = stack.pop()
                val = 0
                if ch == "+":
                    val = t2 + t1
                elif ch == "-":
                    val = t2 - t1
                elif ch == "*":
                    val = t2 * t1
                elif ch == "/":
                    val = int(t2 / t1)
                stack.append(val)
        return stack[-1]

