class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        freq = {}
        res = []

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for ke, v in freq.items():
            bucket[v].append(ke)
        
        for i in range(len(bucket) - 1, -1, -1):        
            for n in bucket[i]:
                if len(res) == k:
                    return res 
                res.append(n)

        return res       
    
