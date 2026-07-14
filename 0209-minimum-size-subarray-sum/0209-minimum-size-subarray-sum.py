class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        high = 0
        s = 0
        low = 0
        res = float('inf')
        for high in range (n):
            s = s + nums[high]
            while(s>=target):
                le = high -low + 1
                res = min(res,le)
                s = s - nums[low]
                low = low +1
            high = high + 1
        if(res==float('inf')):
                return 0
        return res
