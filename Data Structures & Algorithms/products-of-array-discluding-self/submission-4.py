class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        l = 0
        while l <= n - 1:
            val = 1
            for i in range(n):
                if  i == l:
                    continue
                else:
                    val *= nums[i]
            l += 1
            res.append(val)
        return res