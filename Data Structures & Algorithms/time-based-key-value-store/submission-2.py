class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        l = 0 
        r = len(self.store[key])-1
        values = self.store[key] 
        while l <= r: 
            mid = (l+r) // 2
            if values[mid][1] > timestamp: 
                r = mid -1
            elif values[mid][1] < timestamp: 
                res = values[mid][0]
                l = mid + 1
            else:
                return values[mid][0]
        
        return res








        
