class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for val in nums:
            if val in count:
                count[val] +=1
            else:
                count[val] = 1
        heap = []
        for key in count:
            heapq.heappush(heap, [count[key], key])
            if len(heap) > k:
                heapq.heappop(heap)
        for index in range(len(heap)):
            heap[index] = heap[index][1]
        return heap

        




        