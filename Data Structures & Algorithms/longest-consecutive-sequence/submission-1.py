class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = {}
        curr_best = 0
        curr_count = 0
        present = set()
        for v in nums:
            present.add(v)

        while present:
            curr = next(iter(present))
            while curr-1 in present:
                curr = curr-1
            curr_count = 0
            while curr in present:
                present.remove(curr)
                curr_count +=1
                curr+=1
            curr_best = max(curr_best, curr_count)
        return curr_best

        