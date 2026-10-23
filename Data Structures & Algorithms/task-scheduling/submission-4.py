class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)
        q = deque() # [count, cycle_number]

        cycle = 0
        while max_heap or q:
            cycle += 1
            if max_heap:
                count = heapq.heappop(max_heap) + 1
                if count != 0:
                    q.append([count, cycle + n])
            else:
                cycle = q[0][1]
            
            if q and q[0][1] == cycle:
                heapq.heappush(max_heap, q.popleft()[0])
        return cycle