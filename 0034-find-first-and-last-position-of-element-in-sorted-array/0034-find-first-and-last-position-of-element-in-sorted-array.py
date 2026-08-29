class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        first = -1

        while(low<=high):
            guess = int((low+high)/2)
            if(nums[guess]<target):
                low = guess+1
            elif(target<nums[guess]):
                high = guess-1
            else:
                first = guess
                high = guess -1
        low = 0
        high = len(nums) - 1
        last = -1

        while(low<=high):
            guess = int((low+high)/2)
            if(nums[guess]<target):
                low = guess+1
            elif(target<nums[guess]):
                high = guess-1
            else:
                last = guess
                low = guess + 1
        return [first, last]
        
