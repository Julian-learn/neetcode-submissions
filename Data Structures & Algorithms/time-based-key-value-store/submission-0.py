class TimeMap:
    def __init__(self):
        self.tmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.tmap.get(key, [])
        for v, ts in values:
            if ts <= timestamp:
                res = v
            else:
                break
        return res
        
