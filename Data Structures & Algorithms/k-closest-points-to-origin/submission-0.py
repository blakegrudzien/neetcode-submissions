class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        key = {}
        distances = []
        answer = []
        for [i,j] in points:
            tmp_dist = (i**2) + (j**2)
            distances.append([tmp_dist, i, j])
        heapq.heapify(distances)
        print(distances)
        for k in range(k):
            dist, i, j = heapq.heappop(distances)
            answer.append([i,j])
           
        return answer

            
        

        