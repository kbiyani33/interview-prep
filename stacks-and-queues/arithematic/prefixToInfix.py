class Solution:
    def preToInfix(self, prefix):
        # Code here
        n = len(prefix)
        stack = []
        for i in range(n-1, -1, -1):
            ch = prefix[i]
            if ch.isalnum():
                stack.append(ch)
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(f"({t1}{ch}{t2})")
        result = []
        while stack:
            result.append(stack.pop())
        
        return "".join(result)