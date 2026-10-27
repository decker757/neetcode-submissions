class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for n in nums:
            heapq.heappush(min_heap, n)
        
        while len(min_heap) > k:
            heapq.heappop(min_heap)
        
        return min_heap[0]