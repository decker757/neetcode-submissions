class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1

        maxLeft, maxRight = height[l], height[r]
        res = 0

        while l < r:
            if maxLeft < maxRight:
                l += 1
                if maxLeft - height[l] > 0:
                    res += maxLeft - height[l]
                maxLeft = max(maxLeft, height[l])
            else:
                r -= 1
                if maxRight - height[r] > 0:
                    res += maxRight - height[r]
                maxRight = max(maxRight, height[r])
        
        return res
