class Solution:
    def removeDuplicates(self, s: str) -> str:
        # stack = []
        # res = []
        # for i in range(len(s)):
        #     if not stack:
        #         stack.append(s[i])
        #         continue
        #     elif(stack[-1]==s[i]):
        #         stack.pop()
        #         continue
        #     stack.append(s[i])
        # while(stack):
        #     res.append(stack[-1])
        #     stack.pop()
        # res.reverse()
        # return "".join(res)
        res =[]
        for c in s:
            if res and res [-1]==c:
                res.pop()
            else:
                res.append(c)
        return "".join(res)

        