class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        s = 0 
        right = 0
        for i in range(len(nums)):
            s += nums[i]
        if s-nums[0]==0:
            return 0

        for i in range(1,len(nums)):
            left +=nums[i-1]
            right = s - left - nums[i]
            if(left==right):
                return i
        return -1