class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height)-1
        water = 0
        while(left<right):
            le = right-left
            h = min(height[left],height[right])
            water = max(water,le*h)
            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
        return water