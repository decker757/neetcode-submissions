class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key=lambda x :x[0])
        ls = [intervals[0]]
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            lastEnd = ls[-1][1]

            if lastEnd > start:
                res += 1
                ls[-1][1] = min(end, lastEnd)
            else:
                ls.append(intervals[i])
        
        return res
                