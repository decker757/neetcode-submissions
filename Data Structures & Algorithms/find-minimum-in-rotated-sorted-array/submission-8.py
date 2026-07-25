class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_num = float('inf')

        while l <= r:
            m = (l + r) // 2
            min_num = min(min_num, nums[m])
            if nums[l] > nums[r]:
                if nums[l] <= nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                return min(min_num, nums[l])

        return min_num