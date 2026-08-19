class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value,timestamp])

        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        l = 0
        r = len(self.store[key])-1
        while l <= r:
            mid = (l+r)//2
            if self.store[key][mid][1] > timestamp:
                r = mid -1 
            elif self.store[key][mid][1] < timestamp:
                res = self.store[key][mid][0]
                l = mid + 1
            else : 
                return self.store[key][mid][0]
        return res


    

