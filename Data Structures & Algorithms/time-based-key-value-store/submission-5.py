class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        l = self.hashmap[key]
        result = ""
        L = 0
        R = len(l) -1
        while L <= R: 
            mid = (L+R)//2
            if l[mid][0] > timestamp: 
                R = mid -1
            elif l[mid][0] < timestamp: 
                result = l[mid][1]
                L = mid + 1
            else : 
                return l[mid][1]
        
        return result




        
