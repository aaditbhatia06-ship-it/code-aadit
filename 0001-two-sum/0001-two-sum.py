class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        f={}
        for i in range(n):
            x = target - nums[i]
            if x in f:
                return [i,f[x]]
            f[nums[i]]=i
        
            

                