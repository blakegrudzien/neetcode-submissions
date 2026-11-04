class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        key = set()
        for val in nums:
            key.add(val)
        curr_best = 0
        while key:
            curr_count = 0
            curr = next(iter(key))
            while curr-1 in key:
                curr -=1
            while curr in key:
                key.remove(curr)
                curr+=1
                curr_count+=1
            curr_best = max(curr_best,curr_count)
        return curr_best



        