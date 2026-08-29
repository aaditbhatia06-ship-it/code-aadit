class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        res =-1
        while(low<=high):
            guess = int((low+high)/2)
            if(nums[guess]>nums[high]):
                low = guess+1
            else:
                res = guess
                high = high-1
        return nums[res]

