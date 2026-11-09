class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        res = []

        for num, count in num_map.items():
            bucket[count].append(num)
        
        for i in range(len(bucket) - 1, -1 , -1):
            for n in bucket[i]:
                if len(res) == k:
                    return res
                res.append(n)
        
        return res

