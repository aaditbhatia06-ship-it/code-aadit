class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n= len(fruits)
        res = -1
        f= {}
        k =2
        l = 0
        for h in range (n):
            if fruits[h] not in f:
                f[fruits[h]]=0
            f[fruits[h]]+=1
            
            while len(f)>k:
                f[fruits[l]]-=1
                if(f[fruits[l]]==0):
                    del f[fruits[l]]
                l +=1
                
            if len(f)==k or len(f)<k:
                le = h-l+1
                res = max(res,le)
                
        return res