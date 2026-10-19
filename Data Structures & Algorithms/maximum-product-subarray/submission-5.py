class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, curMin, curMax = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            current = (nums[i], nums[i] * curMin, nums[i] * curMax)
            curMin = min(current)
            curMax = max(current)
            res = max(res, curMax)
        
        return res
