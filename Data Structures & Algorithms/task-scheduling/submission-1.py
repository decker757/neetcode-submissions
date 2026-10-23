class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_heap = []

        for v in freq.values():
            max_heap.append(-v)
        
        heapq.heapify(max_heap)

        q = deque()
        time = 0

        while max_heap or q:
            time += 1
            if max_heap:
                count = heapq.heappop(max_heap) + 1
                if count:
                    q.append([count, time + n])
            else:
                time = q[0][1]

            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        
        return time

        