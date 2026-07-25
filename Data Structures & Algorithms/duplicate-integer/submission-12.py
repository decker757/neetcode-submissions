class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = defaultdict(int)

        for n in nums:
            num_dict[n] += 1
        
        for n in num_dict:
            if num_dict.get(n) > 1:
                return True
        return False