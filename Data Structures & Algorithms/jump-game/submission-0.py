class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        spots_left = nums[0]
        i =1

        for i in range(len(nums)):
            if spots_left == 0:
                return False
            spots_left-=1
            spots_left = max(spots_left, nums[i])
        return True

        