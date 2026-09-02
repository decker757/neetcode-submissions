class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for s in stones:
            heapq.heappush(max_heap, -s)

        while len(max_heap) > 1:
            y, x = -heapq.heappop(max_heap), -heapq.heappop(max_heap)

            if x < y:
                heapq.heappush(max_heap, -(y-x)) 
        
        return -max_heap[0] if len(max_heap) == 1 else 0