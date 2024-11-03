class Solution:
    def postToPre(self, postfix):
        # Code here
        n = len(postfix)
        stack = []
        
        for i in range(n):
            ch = postfix[i]
            if ch.isalnum():
                stack.append(ch)
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(f"{ch}{t2}{t1}")
        return stack[-1]