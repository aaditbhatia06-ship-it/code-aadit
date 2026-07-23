class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        freq = {0:-1}
        n = len(nums)
        zero = 0
        one = 0
        res = 0
        for i in range (n):
            if nums[i]==0:
                zero+=1
            elif nums[i]==1:
                one+=1
            dif = one - zero
            if dif in freq:
                res = max(res,i-freq[dif])
            else:
                freq[dif]=i
        return res
        
            


