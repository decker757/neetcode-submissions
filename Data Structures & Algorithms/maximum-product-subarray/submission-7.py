class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = nums[0], nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            cur = nums[i] * curMax, nums[i] * curMin, nums[i]
            curMin = min(cur)
            curMax = max(cur)
            res = max(res, curMax)
        return res