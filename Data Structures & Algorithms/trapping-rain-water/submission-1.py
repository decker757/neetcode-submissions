class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)
        minLR = [0] * len(height)
        res = 0

        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i - 1], height[i - 1])
        
        for i in range(len(height) - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i + 1])
        
        for i in range(len(minLR)):
            minLR[i] = min(leftMax[i], rightMax[i])

        for i in range(len(minLR)):
            if minLR[i] - height[i] > 0:
                res += minLR[i] - height[i]
        
        return res

            
        


        