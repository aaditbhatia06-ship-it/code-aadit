class Solution:
    def canConstruct(self, rans: str, mag: str) -> bool:
        have = {}
        need ={}
        for i in range(len(rans)):
            if rans[i] not in need:
                need[rans[i]]=0
            need[rans[i]]+=1
        for i in range(len(mag)):
            if mag[i] not in have:
                have[mag[i]]=0
            have[mag[i]]+=1
        for ch in need:
            if ch not in have or have[ch]< need[ch]:
                return False
        return True   