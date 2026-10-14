class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = 100000000
        while l <= r:
            m = (l + r) // 2
            res = min(nums[m], res)
            if nums[l] > nums[r]:
                if nums[l] <= nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                r = m - 1
        return res
