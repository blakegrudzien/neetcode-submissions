class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.store:
            return ""
        upper = len(self.store[key])-1
        lower = 0
        curr_best = -1
        
        while upper >= lower:
            mid = (upper + lower)//2
            if self.store[key][mid][0] > timestamp:
                upper = mid-1
            else:
                curr_best = mid
                lower = mid+1
        if curr_best == -1:
            return ""
        return self.store[key][curr_best][1]
        
