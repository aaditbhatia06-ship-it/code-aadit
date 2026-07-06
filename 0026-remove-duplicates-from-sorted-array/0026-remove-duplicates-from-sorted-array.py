class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        officer = 0
        cm = 1
        # element = 1
        n = len(nums)
        while(cm<n):
            if (nums[cm]==nums[cm-1]):
                cm = cm + 1
                continue
            else :
                nums[officer+1]=nums[cm]
                officer = officer+1
                cm = cm +1
                # element += 1
        # return element
        return officer +1