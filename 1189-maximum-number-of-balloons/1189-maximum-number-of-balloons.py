class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        need = {}
        need['b'] =1
        need['a'] =1
        need['l'] =2
        need['o'] =2
        need['n'] =1
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
