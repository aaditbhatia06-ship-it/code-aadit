class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        bestend = nums[0]
        ans = abs(nums[0])
        alt = nums[0]
        for i in range (1, len(nums)):
            c1 = nums[i]
            c2 = bestend + nums[i]
            bestend = max(c1,c2)
            c3 = alt + nums[i]
            c4 = nums[i]
            alt = min(c3,c4)
            
            ans = max(ans,max(abs(bestend),abs(alt)))
        return ans
