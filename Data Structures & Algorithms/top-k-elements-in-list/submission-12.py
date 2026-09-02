class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        hm = Counter(nums)
        res = []

        for n in hm:
            key = hm[n]
            bucket[key].append(n)
        
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                if len(res) == k:
                    return res
                res.append(num)

        return res