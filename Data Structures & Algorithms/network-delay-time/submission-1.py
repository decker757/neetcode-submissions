class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)

        for u, v, w in times:
            adjList[u].append((v, w))

        min_heap = [(0, k)]
        visited = set()
        res = 0
        while min_heap:
            t, node = heapq.heappop(min_heap)

            if node not in visited:
                visited.add(node)
                res = t
                for v, w in adjList[node]:
                    if v not in visited:
                        heapq.heappush(min_heap, (w + t, v))
        
        return res if len(visited) == n else -1