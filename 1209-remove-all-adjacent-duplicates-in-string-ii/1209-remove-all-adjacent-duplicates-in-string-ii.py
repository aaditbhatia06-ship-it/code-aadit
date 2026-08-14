class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        n = len(s)
        stack = []
        for i in range(n):
            c = s[i]
            if not stack:
                stack.append([s[i],1])
                continue
            if(stack[-1][0]!=s[i]):
                stack.append([s[i],1])
            else:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
        ans = ""
        for i in range(len(stack)):
            ans += stack[i][0]*stack[i][1]
        return ans

                  