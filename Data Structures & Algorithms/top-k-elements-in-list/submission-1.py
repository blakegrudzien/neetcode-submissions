class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = [[] for i in range(len(nums)+1)]
        fin = []
        key = {}
        for i in range(len(nums)):
            if nums[i] in key:
                answer[key[nums[i]]].remove(nums[i])
                key[nums[i]] = key[nums[i]] + 1
                answer[key[nums[i]]].append(nums[i])
            else:
                key[nums[i]] = 1
                answer[1].append(nums[i])
        i = len(nums)-1
        while k > 0:
            while answer[i]:
                fin.append(answer[i].pop())
                k-=1
            i-=1
        return fin



        