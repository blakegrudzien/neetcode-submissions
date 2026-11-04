class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        i = 0
        left_curr = 1
        right_curr = 1
        for i in range(len(nums)):
            res[i] *= left_curr
            res[len(nums)-i-1] *= right_curr

            left_curr*=nums[i]
            right_curr*=nums[len(nums)-i-1]




        return res
        