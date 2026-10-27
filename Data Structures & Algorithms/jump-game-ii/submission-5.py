class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_jump = 0
        farthest = 0
        res = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, nums[i] + i)

            if i > farthest:
                return 0

            if cur_jump == i:
                res += 1
                cur_jump = farthest
            
        return res
        