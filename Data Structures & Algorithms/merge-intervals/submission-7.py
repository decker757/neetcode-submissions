class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        st = [intervals[0]]

        for interval in intervals[1:]:
            if st[-1][1] >= interval[0]:
                st[-1][1] = max(st[-1][1], interval[1])
            else:
                st.append(interval)
        
        return st