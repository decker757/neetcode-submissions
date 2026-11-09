class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]

        for i in intervals[1:]:
            start, end = i[0], i[1]
            if res[-1][1] >= start:
                max_end = max(res[-1][1], end)
                res[-1][1] = max_end
            else:
                res.append(i)

        return res