class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach, res, curr = nums[0], 0, 0
    
        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])

            if i == curr:
                res += 1
                curr = max_reach
            
        return res

            
