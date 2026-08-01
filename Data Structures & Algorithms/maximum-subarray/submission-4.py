class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxRes, cur = nums[0], 0

        for n in nums:
            if cur < 0:
                cur = 0
            cur += n
            maxRes = max(maxRes, cur)

        return maxRes          
            