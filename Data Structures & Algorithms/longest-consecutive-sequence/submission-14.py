class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        key = set()
        for v in nums:
            key.add(v)
        
        curr_best = 0
        while key:
            curr = 0
            v = next (iter(key))
            while v-1 in key:
                v-=1
            while v in key:
                key.remove(v)
                v+=1
                curr +=1
            curr_best = max(curr, curr_best)
        return curr_best
        