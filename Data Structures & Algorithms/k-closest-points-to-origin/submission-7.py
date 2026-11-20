class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        for x, y in points:
            dist = (x - 0)**2 + (y - 0)**2
            heapq.heappush(heap, (dist, [x, y]))

        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res