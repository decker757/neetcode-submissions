class TimeMap:

    def __init__(self):
        self.store = defaultdict(list) # k-v pair -> key: [(timestamp, value), ..., (timestamp, value)]
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))        

    def get(self, key: str, timestamp: int) -> str:
        # we want to find the max timestamp if timestamp doesn't exist
        if key not in self.store:
            return ""
        
        values = self.store[key]
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][0] > timestamp:
                r = m - 1
            elif values[m][0] == timestamp:
                return values[m][1]
            else:
                l = m + 1
        
        return values[r][1] if values[r][0] <= timestamp else ""

        
        
        