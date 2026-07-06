class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result=[]
        n = len(nums)
        for i in range(n-2):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            j = i+1
            k = n-1
            t = -1 * nums[i]
            while(j<k):
                s = nums[j]+nums[k]
                if(s==t):
                    result.append([nums[i],nums[j],nums[k]])
                    j = j+1
                    k = k-1
                    while(j<n and nums[j]==nums[j-1]):
                        j=j+1
                    while(k>=0 and nums[k]==nums[k+1]):
                        k = k-1
                elif(s<t):
                    j = j+1
                else:
                    k = k-1
        return result