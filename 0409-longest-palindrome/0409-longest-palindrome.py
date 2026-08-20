class Solution:
    def longestPalindrome(self, s: str) -> int:
        f = {}
        odd= False
        ans = 0
        for i in range (len(s)):
            if s[i] not in f:
                f[s[i]]=0
            f[s[i]]+=1
        for ch in f:
            if f[ch]%2 == 0:
                ans+=f[ch]
            else:
                res = f[ch]//2
                ans+=res*2
                odd = True
        if odd is True:
            ans+=1
        return ans
        
        

