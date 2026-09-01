class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, curMin, curMax = nums[0], nums[0], nums[0]

        for n in nums[1:]:
            current = (n, n * curMin, n * curMax)
            curMin = min(current)
            curMax = max(current)
            res = max(res, curMax)
        return res