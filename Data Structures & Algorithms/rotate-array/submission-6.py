class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mod = 0
        start_index = -1
        while mod < len(nums):
            start_index += 1
            prev_value = nums[start_index]
            curr_index = (start_index + k) % len(nums)
            while curr_index != start_index:
                curr_val = nums[curr_index]
                nums[curr_index] = prev_value
                prev_value = curr_val
                curr_index = (curr_index + k) % len(nums)
                mod+=1
            nums[curr_index] = prev_value
            mod+=1
        return nums 
        