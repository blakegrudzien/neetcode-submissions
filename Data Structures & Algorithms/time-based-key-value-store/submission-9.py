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
        lower = 0
        upper = len(self.store[key])-1
        curr_best = -1
        while lower <= upper:
            mid = (lower + upper)//2
            if self.store[key][mid][0] <= timestamp:
                curr_best = mid
                lower = mid+1
            else:
                upper = mid-1
        if curr_best == -1:
            return ""
        return self.store[key][curr_best][1]
        
