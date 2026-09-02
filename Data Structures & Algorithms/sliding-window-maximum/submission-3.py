class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap, res = [], []
        l = 0
        for r in range(len(nums)):
            heapq.heappush(max_heap, (-nums[r], r))
            if r - l + 1 == k:
                while max_heap[0][1] < l:
                    heapq.heappop(max_heap)
                res.append(-max_heap[0][0])
                l += 1
        return res