class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for n in range(len(nums) + 1)]
        res = []

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for n, i in count.items():
            freq[i].append(n)
        
        for i in range(len(freq) - 1, -1 ,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
            
