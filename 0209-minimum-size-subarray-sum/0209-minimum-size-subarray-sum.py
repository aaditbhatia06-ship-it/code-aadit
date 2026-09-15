class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        s = 0
        low = 0
        res = float('inf')
        for high in range (len(nums)):
            s = s + nums[high]
            while(s>=target):
                res = min(res,high-low+1)
                s = s - nums[low]
                low = low +1
        if(res==float('inf')):
                return 0
        return res
