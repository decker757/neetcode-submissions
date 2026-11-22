class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)

        for u, v in sorted(tickets)[::-1]:
            adjList[u].append(v)
        
        stack = ["JFK"]
        res = []

        while stack:
            curr = stack[-1]
            if not adjList[curr]:
                res.append(stack.pop())
            else:
                stack.append(adjList[curr].pop())

        return res[::-1]