class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = [[] for i in range(len(nums)+1)]
        fin = []
        key = {}
        for n in nums:
            key[n] = 1 + key.get(n,0)
        
        for n, c in key.items():
            answer[c].append(n)

        i = len(nums)-1
        while k > 0:
            while answer[i]:
                fin.append(answer[i].pop())
                k-=1
            i-=1
        return fin



        