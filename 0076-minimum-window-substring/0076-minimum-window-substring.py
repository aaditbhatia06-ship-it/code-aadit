class Solution:
    def minWindow(self, s: str, t: str) -> str:
        f ={}
        l = 0
        n = len(t)
        j =  len(s)
        start =0
        freq={}
        res = float('inf')
        for i in range (n):
            if t[i] not in f :
                f[t[i]]=0
            f[t[i]]+=1
        def check(freq, f):
            for ch in f:
                if freq.get(ch, 0) < f[ch]:
                    return False
            return True
            

        for h in range (j):
            if s[h] not in freq:
                freq[s[h]] =0
            freq[s[h]]+=1
            while check(freq,f):
                le = h -  l + 1
                if(res>le):
                    res= le
                    start = l
                freq[s[l]]-=1
                l +=1
            
        if res == float('inf'):
            return ""
        return s[start:start + res]
        
