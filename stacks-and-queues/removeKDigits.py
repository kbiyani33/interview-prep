class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if k==n: return "0"
        if k==0: return num

        stack = [num[0]]
        for i in range(1, n):
            while stack and int(stack[-1]) > int(num[i]) and k>0:
                stack.pop()
                k -= 1
            stack.append(num[i])
        
        while k > 0:
            stack.pop()
            k -= 1 
        ans = "".join(stack).lstrip("0")
        if not ans: return "0"
        return ans
            
