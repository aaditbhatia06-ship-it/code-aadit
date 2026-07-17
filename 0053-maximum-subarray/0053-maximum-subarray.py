class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        ans = nums[0]
        n = len(nums)
        for i in range(1,n):
            c1 = best + nums[i]
            c2 = nums[i]
            best = max(c1,c2)
            ans = max(best,ans)
        return ans