class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curr_best = len(nums)+1
        sliding_sum = 0
        for r in range(len(nums)):
            sliding_sum+=nums[r]
            while l <= r and sliding_sum >= target:
                curr_best = min(curr_best, r-l+1)
                sliding_sum-=nums[l]
                l+=1
        if curr_best == len(nums)+1:
            return 0
        return curr_best


        