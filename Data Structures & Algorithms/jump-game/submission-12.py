class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxJump = 0

        for i in range(n):
            if i > maxJump:
                return False
            maxJump = max(maxJump, nums[i] + i)
            if maxJump >= n - 1:
                return True
        