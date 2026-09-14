class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = 0
        for i in range(k):
            s += nums[i]
        res = s
        low = 0
        high = k
        while(high<len(nums)):
            s = ((s-nums[low]+nums[high]))
            res = max(res,s)
            low +=1
            high+=1
        return res/k
    