class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach = 0
        res = 0
        curr = 0
        for i in range(len(nums) - 1):
            max_reach = max(max_reach, nums[i] + i)

            if i == curr:
                res += 1
                curr = max_reach

        return res

            
        