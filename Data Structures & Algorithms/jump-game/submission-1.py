class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, n = 0, len(nums)
        farthest = 0

        while i < n:
            if i > farthest:
                return False
            
            farthest = max(farthest, nums[i] + i)
            if farthest >= n - 1:
                return True
            
            i += 1

        return False
