class Solution:
    def postToInfix(self, postfix):
        # Code here
        stack = []
        result = []
        n = len(postfix)
        
        for i in range(n):
            # operands are pushed to stack
            ch = postfix[i]
            if ch.isalnum():
                stack.append(ch)
            else:
                # take out the 2 top elements from the stack 
                # then add the current operator
                el1 = stack.pop()
                el2 = stack.pop()
                stack.append("(" + el2 + ch + el1 + ")") # el2 first since it's LIFO
        
        while stack:
            result.append(stack.pop())
        return "".join(result)