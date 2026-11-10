class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x, y in points:
            distances.append([((x**2) + (y**2)),x,y])
        heapq.heapify(distances)
        print(distances)
        res = []
        for i in range(k):
            curr = heapq.heappop(distances)
            res.append([curr[1],curr[2]])
        return res

        