class TimeMap:
    def __init__(self):
        self.tmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.tmap.get(key, [])
        l = 0
        r = len(values) - 1
        while l <= r:
            mid = (l + r) // 2 
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
                res = values[mid][0]
        return res