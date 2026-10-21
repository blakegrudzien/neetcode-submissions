class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count =  [[] for _ in range(len(nums)+1)]

        key = {}

        for v in nums:
            if v in key:
                count[key[v]].remove(v)
                key[v] +=1
                count[key[v]].append(v)
            else:
                key[v] = 1
                count[1].append(v)

        res = []
        index = len(nums)-1
        while len(res) < k:
            while count[index] and len(res) < k:
                res.append(count[index].pop())
            index-=1
        return res
            


            

            
        