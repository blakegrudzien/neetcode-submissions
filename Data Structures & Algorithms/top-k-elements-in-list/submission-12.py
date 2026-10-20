class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = {}
        heapq.heapify(heap)
        

        for v in nums:
            if v in count:
                count[v][0]-=1
            else:
                count[v] = [-1,v]
        
        for c in count:
            heapq.heappush(heap, count[c])

        res = []
        for i in range(k):
            count, val = heapq.heappop(heap)
            res.append(val)
        return res

            
        
            

        