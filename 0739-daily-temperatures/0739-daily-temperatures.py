class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        res = [-1]*len(temp)
        n = len(temp)
        res[n-1]=0
        stack.append(n-1)
        for i in range(n-2,-1,-1):
            while(stack and temp[stack[-1]]<=temp[i]):
                stack.pop()
            if(not stack):
                res[i]=0
            else:
                res[i] = stack[-1]-i
            stack.append(i)
        return res


