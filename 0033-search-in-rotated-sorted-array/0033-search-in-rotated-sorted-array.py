class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0 
        n = len(nums)
        high = n-1
        while(low<=high):
            guess = int((low+high)/2)
            if(nums[guess]==target):
                return guess
            if(nums[guess]>nums[n-1]):
                if(nums[guess]<target):
                    low = guess+1
                else:
                    if(nums[0]>target):
                        low = guess+1
                    else:
                        high = guess -1
            else:
                if(nums[guess]>target):
                    high = guess -1
                else:
                    if(nums[n-1]<target):
                        high = guess-1
                    else:
                        low = guess +1
        return -1

