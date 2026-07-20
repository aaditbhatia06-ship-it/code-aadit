class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        su = 0
        freq={}
        freq[0]=1
        res = 0
        for i in range (len(nums)):
            su += nums[i]
            ques = su - k
            if ques in freq:
                fr = freq[ques]
            else:
                fr =0
            res+=fr
            if su not in freq:
                freq[su] = 0
            freq[su] += 1
        return res
