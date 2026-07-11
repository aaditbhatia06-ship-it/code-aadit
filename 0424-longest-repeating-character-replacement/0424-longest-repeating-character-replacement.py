class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        f = {}
        n = len(s)
        l = 0
        maxf=0
        res =0
        for h in range (n):
            if s[h] not in f:
                f[s[h]]=0
            f[s[h]] += 1

            le = h-l+1
            maxf = max(maxf,f[s[h]])
            diff = le - maxf
            while(diff>k):
                f[s[l]] -= 1
                l +=1
                maxf = max(maxf,f[s[h]])
                le = h-l+1
                diff = le - maxf
            if diff==k or diff<k:
                le = h-l+1
                res = max(res,le)
        return res

            