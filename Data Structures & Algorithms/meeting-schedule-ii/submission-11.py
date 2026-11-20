"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
            1. sort by start time
            2. st = [(0, 40)] -> iterate through intervals[1:] 
                - check st[-1][1] > interval[0]
                    - append
                    - pop
            3. return len(st)
        """
        if len(intervals) == 0: return 0

        intervals.sort(key=lambda x:x.start)
        heap = []
        
        for interval in intervals:
            if heap and heap[0] <= interval.start:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)
        
        return len(heap)