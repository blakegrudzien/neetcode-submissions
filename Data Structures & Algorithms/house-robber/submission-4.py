class Solution:
    def rob(self, nums: List[int]) -> int:
        

        best = 0
        for i in range(len(nums)):
            if i<2:
                nums[i] = nums[i]
            elif i == 2:
                nums[i] = nums[i] + nums[0]
            else:
                nums[i] = nums[i] + max(nums[i-2],nums[i-3])
            best = max(best, nums[i])
        return best

                
        