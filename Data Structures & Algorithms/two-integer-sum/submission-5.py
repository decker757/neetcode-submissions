class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, n in enumerate(nums):
            complement = target - n

            if complement in dic:
                return [dic[complement], i]
            dic[n] = i