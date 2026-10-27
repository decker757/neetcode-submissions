class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        minLR = [0] * len(height)
        n = len(height)

        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i - 1], height[i - 1])
        
        for i in range(n - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i + 1])
        
        for i in range(n):
            minLR[i] = min(maxRight[i], maxLeft[i])
        
        res = 0
        for i in range(n):
            if minLR[i] - height[i] > 0:
                res += minLR[i] - height[i]
        
        return res