class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        stack = []
        res = []
        n = len(s)
        i = 0
        while (i<n and i < k):
            stack.append(s[i])
            i+=1
        while stack:
            res.append(stack.pop())
        while i<n:
            res.append(s[i])
            i+=1
        return "".join(res)
