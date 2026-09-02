class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        suff = 1
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suff
            suff *= nums[i]
        
        return res
            