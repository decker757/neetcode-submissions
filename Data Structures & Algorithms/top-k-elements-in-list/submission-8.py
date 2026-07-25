class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        arr = []
        num_dict = {}

        for n in nums:
            if n not in num_dict:
                num_dict[n] = 0
            num_dict[n] += 1

        for key, value in num_dict.items():
            arr.append([value,key])
        arr.sort()
        
        while len(res) < k:
            res.append(arr.pop()[1])

        return res