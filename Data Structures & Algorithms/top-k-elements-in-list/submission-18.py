class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[]for _ in nums]
        key = {}

        for val in nums:
            if val not in key:
                count[0].append(val)
                key[val] = 0
            else:
                count[key[val]].remove(val)
                key[val]+=1
                count[key[val]].append(val)
        res = []
        index = len(count)-1
        while len(res) < k:
            while len(res) < k and count[index]:
                res.append(count[index].pop())
            index-=1

        return res
        