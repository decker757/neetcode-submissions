class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[n] = i
        