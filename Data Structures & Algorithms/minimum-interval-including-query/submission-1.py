class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals = sorted(intervals,key = lambda x: (x[0],x[1]-x[0]))
        query = [0] * len(queries)
        for i in range(len(queries)):
            query[i] = [queries[i],i]
        query = sorted(query)
        heap = []
        res = [0] * len(query)
        index = 0
        for q in query:
            while index<len(intervals) and q[0]>=intervals[index][0]:
                temp = intervals[index]
                heapq.heappush(heap, [temp[1]-temp[0]+1,temp[1]])
                index+=1
            while heap and q[0]>heap[0][1]:
                heapq.heappop(heap)
            if not heap:
                res[q[1]] = -1
            else:
                res[q[1]] = heap[0][0]
        return res

        