class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[l]
        while l <= r:
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[l] > nums[r]:
                if nums[m] >= nums[l]:
                    l += 1
                else:
                    r -= 1
            else:
                if nums[m] <= nums[l]:
                    r -= 1
                else:
                    l += 1
            
        return res
