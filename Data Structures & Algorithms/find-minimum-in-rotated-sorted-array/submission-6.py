class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        if nums[l] <= nums[r]:
            return nums[l]


        while l< r:
            if nums[l] < nums[l-1]:
                return nums[l]
            if nums[r] < nums[r-1]:
                return nums[r]
            m = (l+r)//2
            if nums[m] < nums[m-1]:
                return nums[m]
            if nums[m] > nums[l]:
                l = m+1

            elif nums[m] < nums[l]:
                r = m-1

            
            

        