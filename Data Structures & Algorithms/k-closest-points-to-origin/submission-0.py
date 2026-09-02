class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hm = {}
        res = []
        min_heap = []

        for p in points:
            distance_from_origin = math.sqrt((p[0] - 0)**2 + (p[1] - 0)**2)     
            key = tuple(p)
            hm[key] = hm.get(key, 0) + distance_from_origin
        
        for key in hm:
            heapq.heappush(min_heap, (hm[key], key))
        
        while k > 0:
            key = heapq.heappop(min_heap)[1]
            res.append(key)
            k -= 1
        
        return res