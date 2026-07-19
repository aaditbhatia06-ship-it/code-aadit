class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        minans = nums[0]
        maxans = nums[0]
        ans = nums[0]
        s = 0
        circmin = nums[0]
        circmax=nums[0]
        for j in range(len(nums)):
                s = s+nums[j]
        for i in range (1,len(nums)):
            circmax = max(nums[i],circmax + nums[i] )
            maxans = max(circmax,maxans)
           
            circmin = min(circmin + nums[i],nums[i])
            minans = min (minans,circmin)
            ans = max(maxans,s-minans)
        if maxans < 0:
            return maxans
        return ans
                
                