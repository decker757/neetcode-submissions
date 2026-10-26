class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list) # key: [(timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.time_map[key]) - 1

        while l <= r:
            m = (l + r) // 2
            if self.time_map[key][m] == timestamp:
                return self.time_map[key][m][0]
            elif self.time_map[key][m][1] > timestamp:
                r = m - 1
            else:
                l = m + 1

        if r >= 0:
            return self.time_map[key][r][0]
        return ""
