class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr = nums[0]
        curr_max = nums[0]

        l = 0
        r = 1
        while r< len(nums):
            
            curr += nums[r]
            #print(l, "  " , r)

        
            while l<r and (curr < 0 or nums[l] < 0):
                curr-=nums[l]
                l+=1
            curr_max = max(curr_max, curr)
            r+=1
        return curr_max 
            

        
        