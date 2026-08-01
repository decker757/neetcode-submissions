class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxRes, curMax, curMin = nums[0], nums[0], nums[0]

        for r in range(1, len(nums)):
            n = nums[r]
            current = (n, curMax * n, curMin * n)
            curMax = max(current)
            curMin = min(current)
            maxRes = max(maxRes, curMax)

        return maxRes
