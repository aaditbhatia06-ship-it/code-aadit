# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         f = {}
#         res = 0
#         n = len(s)
#         l = 0
#         for h in range(n):
#             if s[h] not in f:
#                 f[s[h]]=0
#             f[s[h]]+=1
            
#             k = h-l+1
#             while len(f)<k:
#                 f[s[l]] -=1
#                 if(f[s[l]]==0):
#                     del f[s[l]]
#                 l += 1
#                 k = h-l+1
#             if len(f)==k:
#                 le = h-l+1
#                 res = max(res,le)
#         return res
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        l = 0
        ans = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1

            while freq[s[r]] > 1:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1

            ans = max(ans, r - l + 1)

        return ans