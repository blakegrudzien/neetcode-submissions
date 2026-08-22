class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        key = {}
        heap = []
        ans = []
        for x, y in points:
            dist = (x*x) + (y*y)
            while dist in heap:
                dist += .0001
            heapq.heappush(heap, dist)
            key[dist] = [x,y]
        
        while k > 0:
            d = heapq.heappop(heap)
            ans.append(key[d])
            k-=1

        return ans





        
        