class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i, n = 0, len(intervals)
        res = []
        start, end = newInterval[0], newInterval[1]

        while i < n and intervals[i][1] < start:
            res.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= end:
            start = min(intervals[i][0], start)
            end = max(end, intervals[i][1])
            i += 1
        res.append([start, end])
        
        while i < n:
            res.append(intervals[i])
            i += 1
        return res