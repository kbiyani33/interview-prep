class Solution:
    def preToPost(self, prefix):
        # Code here
        if not prefix: return ""
        stack = []
        n = len(prefix)
        for i in range(n-1, -1, -1):
            ch = prefix[i]
            if ch.isalnum():
                stack.append(ch)
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(f"{t1}{t2}{ch}")
        return stack[-1]