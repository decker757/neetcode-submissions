class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = {}

        for index, n in enumerate(nums):
            complement = target - n

            if complement in difference:
                return [difference[complement], index]
            else:
                difference[n] = index 
        
        return []