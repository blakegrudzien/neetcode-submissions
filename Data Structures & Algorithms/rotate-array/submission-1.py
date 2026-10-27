class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = [0] * len(nums)
        for i in range(len(nums)):
            destination = (i + k) % len(nums)
            temp[destination] = nums[i]
        
        for i in range(len(nums)):
            nums[i] = temp[i]
        return nums

        