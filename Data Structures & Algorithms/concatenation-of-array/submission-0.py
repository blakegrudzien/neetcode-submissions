class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        n = len(nums)
        for i in range(n):
            nums.append(nums[i])

        return nums
        