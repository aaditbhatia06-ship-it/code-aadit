class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 0 
        n = len(arr)
        high = n-1
        first = -1
        while(low<=high):
            guess= int((low+high)/2)
            if(arr[guess]<arr[guess+1]):
                low = guess+1
            else:
                first = guess
                high = guess - 1
        return first
