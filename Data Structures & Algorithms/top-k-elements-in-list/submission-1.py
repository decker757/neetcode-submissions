class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        res = []
        for num in nums:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1
        
        sorted_keys = sorted(dic, key = lambda x : dic[x], reverse = True)

        return sorted_keys[:k]