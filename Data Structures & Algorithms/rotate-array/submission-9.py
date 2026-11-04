class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[::-1]
        nums[0:(k%len(nums))] = nums[0:(k%len(nums))][::-1]
        nums[(k%len(nums)):len(nums)] = nums[(k%len(nums)):len(nums)][::-1]
        return  
        