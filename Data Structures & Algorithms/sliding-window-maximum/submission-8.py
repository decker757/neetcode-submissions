class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        for i, n in enumerate(nums):
            while q and q[-1][1] < n:
                q.pop()
            q.append((i, n))

            if q[0][0] <= i - k:
                q.popleft()

            if i >= k - 1:
                res.append(q[0][1])

        return res 