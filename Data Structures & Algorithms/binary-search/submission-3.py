class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        
        if nums[r] == target:
                return r
        if nums[l] == target:
            return l
        

        while r-l > 1:
            mid = (r + l) // 2
            if target > nums[mid]:
                l = mid
            else:
                r = mid
            if nums[r] == target:
                return r
            if nums[l] == target:
                return l
        return-1
        