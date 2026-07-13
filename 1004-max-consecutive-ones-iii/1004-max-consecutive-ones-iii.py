class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        zeros = 0
        res = 0

        for h in range(len(nums)):
            if nums[h] == 0:
                zeros += 1

            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            res = max(res, h - l + 1)

        return res

            