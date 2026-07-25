class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = 0
        currSum = maxNumber = nums[0]

        for num in nums[1:]:
            currSum = max(num, currSum + num)
            maxNumber = max(maxNumber, currSum)

        return maxNumber