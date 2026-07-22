class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq ={}
        freq[0] = 1
        ans = 0
        s = 0
        for i in range(len(nums)):
            s+=nums[i]
            rem = s % k
            if (rem<0):
                rem +=k
            if rem not in freq:
                freq[rem]=0
            ans += freq[rem]
            freq[rem]+=1
        return ans

        
        