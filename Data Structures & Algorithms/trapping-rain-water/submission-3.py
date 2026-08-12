class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        minLR = [0] * len(height)
        res = 0

        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i - 1], height[i - 1])
        
        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i + 1])

        for i in range(len(height)):
            minLR[i] = min(maxLeft[i], maxRight[i])
        
        for i in range(len(height)):
            if minLR[i] - height[i] > 0:
                res += minLR[i] - height[i]

        return res