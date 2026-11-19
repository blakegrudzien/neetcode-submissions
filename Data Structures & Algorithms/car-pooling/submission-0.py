class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key = lambda x: x[1])
        heap = []
        for t in trips:
            while heap and heap[0][0]<=t[1]:
                temp = heapq.heappop(heap)
                capacity+=temp[1]
            heapq.heappush(heap,[t[2],t[0]])
            capacity -= t[0]
            if capacity<0:
                return False
        return True
        