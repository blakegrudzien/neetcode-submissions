class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        ans = []
        for x, y in points:
            dist = (x*x) + (y*y)

            heap.append([dist, x, y])
        heapq.heapify(heap)

        
        while k > 0:
            d, x, y = heapq.heappop(heap)
            ans.append([x,y])
            k-=1

        return ans





        
        