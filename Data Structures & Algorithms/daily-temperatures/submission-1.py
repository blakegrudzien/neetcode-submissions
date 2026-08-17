class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        h = []
        heapq.heapify(h)

        for i in range(len(temperatures)):
            while h and (temperatures[i],0) > h[0]:
                (l,j) = heapq.heappop(h)
                temperatures[j] = i-j
            heapq.heappush(h,(temperatures[i],i))
        while h:
            (l,j) = heapq.heappop(h)
            temperatures[j] = 0

        return temperatures
            
        