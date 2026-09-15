class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        f = {}
        freq = {}
        for i in range(len(s)):
            if s[i] not in f:
                f[s[i]]=0
            f[s[i]] +=1
        for i in range(len(t)):
            if t[i] not in freq:
                freq[t[i]]=0
            freq[t[i]] +=1
        for ch in f :
            if ch not in freq or f[ch] != freq[ch]:
                return False
        return True
        
