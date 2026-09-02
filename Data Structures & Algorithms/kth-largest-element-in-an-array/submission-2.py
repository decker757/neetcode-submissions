class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        res = 0

        for n in nums:
            heapq.heappush(max_heap, -n)
        
        while k > 0:
            res = heapq.heappop(max_heap)
            k -= 1
        
        return -res