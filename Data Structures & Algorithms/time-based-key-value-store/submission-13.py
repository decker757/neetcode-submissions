from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list) # {"key": [(value, timestamp)]}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store: return ""
        
        values = self.store.get(key, [])
        if values == []: return ""
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2

            if values[m][1] <= timestamp:
                l = m + 1
            else:
                r = m - 1
        
        return values[r][0] if r >= 0 else ""
    
