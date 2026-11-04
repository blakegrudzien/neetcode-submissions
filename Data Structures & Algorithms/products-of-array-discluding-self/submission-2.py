class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        left[0] = nums[0]
        right[len(nums)-1] = nums[len(nums)-1]
        i = 1
        while i < len(nums):
            left[i] = left[i-1] * nums[i]
            right[len(nums)-i-1] = right[len(nums)-i] * nums[len(nums)-i-1]
            i+=1
        res = [1] * len(nums)
        i = 1
        res[0] = right[1]
        res[len(nums)-1] = left[len(nums)-2]
        while i < len(nums)-1:
            res[i] = left[i-1] * right[i+1]
            i+=1

        return res
        