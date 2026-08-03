class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        res = 0
        for n in nums:
            heapq.heappush(heap, -n)
        
        while k > 0:
            res = heapq.heappop(heap)
            k -= 1

        return -res