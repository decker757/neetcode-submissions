class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = {}

        for n in nums:
            if n not in hm:
                hm[n] = 0
            hm[n] += 1
        
        for n in hm.keys():
            if hm[n] > 1:
                return True
        return False