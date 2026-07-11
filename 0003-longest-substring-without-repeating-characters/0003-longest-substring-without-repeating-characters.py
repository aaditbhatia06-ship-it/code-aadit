class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        f = {}
        res = 0
        n = len(s)
        l = 0
        h = 0 
        for h in range(n):
            if s[h] not in f:
                f[s[h]]=0
            f[s[h]]+=1
            
            k = h-l+1
            while len(f)<k:
                f[s[l]] -=1
                if(f[s[l]]==0):
                    del f[s[l]]
                l += 1
                k = h-l+1
            if len(f)==k:
                le = h-l+1
                res = max(res,le)
        return res
        