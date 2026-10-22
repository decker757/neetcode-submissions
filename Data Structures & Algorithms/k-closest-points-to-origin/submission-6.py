class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        x1 = y1 = 0
        res = []

        for x, y in points:
           dist = (x1 - x)**2 + (y1 - y)**2
           heapq.heappush(min_heap, (dist, [x, y]))

        while k > 0:
            
            res.append(heapq.heappop(min_heap)[1])
            k -= 1
        
        return res