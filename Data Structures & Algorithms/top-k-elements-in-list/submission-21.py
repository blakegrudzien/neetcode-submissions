class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for val in nums:
            if val in count:
                count[val]+=1
            else:
                count[val] = 1
        
        bucket = [[] for _ in nums]
        for key in count:
            bucket[count[key]-1].append(key)
        
        res = []
        index = len(bucket)-1
        while len(res)<k:
            while len(res) < k and bucket[index]:
                res.append(bucket[index].pop())
            index-=1
        return res



        