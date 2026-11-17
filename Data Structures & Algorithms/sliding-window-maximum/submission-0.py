class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        r = 0
        heap = []
        key = {}
        while r<k:
            key[nums[r]] = key.get(nums[r],0)+1
            heapq.heappush(heap, (nums[r]*(-1)))
            r+=1
        res = []
        l = 0
        while r< len(nums):
            while (heap[0])*(-1) not in key:
                heapq.heappop(heap)
            res.append(heap[0]*(-1))
            if key[nums[l]] == 1:
                key.pop(nums[l])
            else:
                key[nums[l]]-=1
            key[nums[r]] = key.get(nums[r],0)+1
            heapq.heappush(heap, (nums[r]*(-1)))
            r+=1
            l+=1
        while (heap[0])*(-1) not in key:
            heapq.heappop(heap)
        res.append(heap[0]*(-1))
        return res

            
        