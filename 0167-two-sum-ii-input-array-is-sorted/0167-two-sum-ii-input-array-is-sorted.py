class Solution(object):
    def twoSum(self, nums, target):
        
        i = 0
        j = len(nums)-1
        while(i<j):
            sum= nums[i] + nums[j]
            if(sum==target):
                return (i+1) , (j+1)
            elif(sum<target):
                i=i+1
            elif(sum>target):
                j =j -1       