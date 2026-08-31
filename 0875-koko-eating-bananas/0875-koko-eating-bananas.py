class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while(low <= high):
            hours = 0
            mid = int((low+high)/2)
            for i in range (len(piles)):
                hours += int(piles[i]/mid)
                if(piles[i]%mid != 0):
                    hours+=1
            if(hours<=h):
                high = mid - 1
            else:
                low = mid + 1
        return low
                 