class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}

        for n in nums:
            if n not in num_dict:
                num_dict[n] = 0
            num_dict[n] += 1
        
        for k in num_dict:
            if num_dict[k] > 1:
                return True
        return False