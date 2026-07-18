class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxend = nums[0]
        minend = nums[0]
        ans = nums[0]
        for i in range (1,len(nums)):
            c1 =nums[i]
            c2 = minend * nums[i]
            c3 = maxend *nums[i]
            maxend = max(c1,max(c2,c3))
            minend =  min(c1,min(c2,c3))
            ans = max(ans,max(maxend,minend))
        return ans