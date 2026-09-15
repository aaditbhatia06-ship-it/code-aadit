class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        su = int(n*(n+1)/2)
        s = 0
        for i in range(n):
            s+=nums[i]
        return su-s

       

