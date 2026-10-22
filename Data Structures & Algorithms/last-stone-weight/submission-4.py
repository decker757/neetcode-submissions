class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for st in stones:
            heapq.heappush(max_heap, -st)
        
        while len(max_heap) > 1:
            print(max_heap)
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)

            if x == y:
                continue
            elif x < y:
                y = y - x
                heapq.heappush(max_heap, -y)
        
        if len(max_heap) == 0: return 0
        print(max_heap)
        return -max_heap[0]
