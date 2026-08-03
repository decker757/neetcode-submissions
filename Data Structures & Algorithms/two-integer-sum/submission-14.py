class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in hm:
                return [hm[complement], i]
            hm[n] = i
        return []