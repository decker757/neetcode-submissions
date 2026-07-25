class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        result = []
        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n] += 1
        pairs = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        result = [key for key, _ in pairs[:k]]
        return result