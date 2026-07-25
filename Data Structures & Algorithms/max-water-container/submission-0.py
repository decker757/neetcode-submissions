class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        trappedWater = 0
        maxTrap = 0
        
        while left < right:
            trappedWater = min(heights[left],heights[right]) * (right - left)
            maxTrap = max(maxTrap, trappedWater)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1
        return maxTrap