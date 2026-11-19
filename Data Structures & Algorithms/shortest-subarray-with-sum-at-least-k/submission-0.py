class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        window = 0
        curr_best = len(nums)+1
        for r in range(len(nums)):
            window+=nums[r]
            if window < 0:
                l = r+1
                window = 0
            while window >= k:
                curr_best = min(curr_best,(r-l+1))
                window-=nums[l]
                l+=1
                while l<=r and nums[l]<=0:
                    window-=nums[l]
                    l+=1
        if curr_best == len(nums)+1:
            return -1
        return curr_best
            

        

