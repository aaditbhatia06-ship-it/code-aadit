class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        need = {
        'b':1,
        'a':1,
        'l':2,
        'o':2,
        'n':1
        }
        have = {}
        for i in range(len(text)):
            if text[i] not in have:
                have[text[i]]=0
            have[text[i]]+=1
        res = float("inf")
        for char in need :
            if char not in have:
                return 0
            res = int(min(res,have[char]/need[char]))
        return res
