class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        currWater = 0
        maxWater = 0
        while l <= r:
            currWater = min(heights[l],heights[r]) *(r-l)
            maxWater = max(maxWater, currWater)
            if heights[l] < heights[r]:    
                l += 1
            else:
                r -= 1


        return maxWater