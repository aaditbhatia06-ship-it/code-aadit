class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        f ={}
        for i in range(n):
            if s[i] not in f:
                f[s[i]]=0
            f[s[i]]+=1
        for i in range(n):
            if(f[s[i]]==1):
                return i
        return -1