class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        for i in range(len(nums)):
            if i != 0 and i != 1 and i != 2:
                nums[i] += max(nums[i-2], nums[i-3])
            if i == 2:
                nums[i] += nums[0]
        return max(nums[len(nums)-1], nums[len(nums)-2])
                

        