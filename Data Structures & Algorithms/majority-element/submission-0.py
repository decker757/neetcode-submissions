class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorityLength = len(nums)/2
        hm = {}
        nums.sort()

        for n in nums:
            if n not in hm:
                hm[n] = 0
            hm[n] += 1

        for k in hm.keys():
            if hm[k] > majorityLength:
                return k
        