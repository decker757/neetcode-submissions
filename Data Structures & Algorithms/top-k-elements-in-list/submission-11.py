class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            hm[n] = 1 + hm.get(n, 0)
        
        for n, c in hm.items():
            freq[c].append(n)

        res = []
       
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                if len(res) == k:
                    return res
                res.append(num)

        return res