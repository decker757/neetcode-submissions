class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = res = 0

        pre = 1
        for r in range(len(nums)):
            pre *= nums[r]
            while l <= r and pre >= k:
                pre //= nums[l]
                l += 1
            res += (r - l + 1)
        return res
