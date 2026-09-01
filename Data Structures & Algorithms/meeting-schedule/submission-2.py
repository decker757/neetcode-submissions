"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)

        for i in range(1, len(intervals)):
            start2 = intervals[i].start
            end1 = intervals[i - 1].end

            if start2 < end1:
                return False
            
        return True