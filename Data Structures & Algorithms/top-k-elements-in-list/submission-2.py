class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        items = list(freq.items())

        def get_count(pairs):
            return pairs[1]
        
        items.sort(key=get_count ,reverse=True)

        for i in range(k):
            res.append(items[i][0])
        
        return res