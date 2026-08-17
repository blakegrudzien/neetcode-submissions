class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_count = 0
        max_count = 0

        for val in nums:
            if val == 1:
                curr_count +=1
            else:
                max_count = max(max_count, curr_count)
                curr_count = 0
        return max(max_count, curr_count)        